from tkinter import *
import tkinter.messagebox
from pytube import YouTube
import os

root = Tk()
root.geometry('400x160')
root['bg']='#004038'
root.title('Youtube Downloader')
root.resizable(False, False)

def clear_text():
   get_video_input.delete(0, END)
   get_audio_input.delete(0, END)

input_video_url = StringVar()
input_audio_url = StringVar()

def download(get_video_link=input_video_url.get() if input_video_url else None, get_audio_link=input_audio_url.get() if input_audio_url else None):

    video_link = input_video_url.get()
    audio_link = input_audio_url.get()

    try:
        if video_link:
            yt_video = YouTube(video_link)
            print('\nStart downloading... Please wait...\n')
            # yvd = yt_video.streams.first()
            yvd = yt_video.streams.get_highest_resolution()
            yvd.download() #"C:\\Users\\Username\\Downloads\\Videos"

            print(f'\n{yt_video.title} Downloaded successfully')
            result_label.config(text=f"{yt_video.title} video downloaded")
            # tkinter.messagebox.showinfo("Download finished", f"{yt_video.title} is saved on your pc")
            clear_text()
    except:
        result_label.config(text="An error occurred. Please check the file and try again.")

    try:
        if audio_link:
            yt_audio = YouTube(audio_link)
            print('\nStart downloading... Please wait...\n')

            yad = yt_audio.streams.filter(only_audio=True).first()
            out_file = yad.download() #"C:\\Users\\Username\\Downloads\\Audios"
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print(f'\n{yt_audio.title} Downloaded successfully')
            result_label.config(text=f"{yt_audio.title} audio downloaded")
            # tkinter.messagebox.showinfo("Download finished", f"{yt_audio.title} is saved on your pc")
            clear_text()
    except:
        result_label.config(text="An error occurred. Please check the file and try again.")

    if 'https://www.youtube.com/' not in video_link and 'https://www.youtube.com/' not in audio_link:
        result_label.config(text="You didn't choose video-url")
        # tkinter.messagebox.showinfo("File not found", "Choose video-url to download")
        clear_text()

#VIDEO
video_label = Label(root, text = 'Video Downloader', bg = '#004038', fg = 'white').pack()
get_video_input = Entry(root, width = 100, textvar = input_video_url)
get_video_input.pack()

#AUDIO
audio_label = Label(root, text = 'Audio Downloader', bg = '#004038', fg = 'white').pack()
get_audio_input = Entry(root, width = 100, textvar = input_audio_url)
get_audio_input.pack()

#CONFIRM
Button(root, width = 80, bg = 'green', fg = 'white', relief = 'sunken', text = 'Download', command = download).pack()

#CLEAR FIELDS
Button(root, text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)

result_label = Label(root, text="", bg='#004038', fg='white')
result_label.pack()

root.mainloop()
