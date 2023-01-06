from tkinter import *
import tkinter.messagebox
from pytube import YouTube
from sys import argv
import os

root = Tk()
root.geometry('400x150')
root['bg']='#004038'
root.title('Youtube Downloader')



def clear_text():
   get_video_input.delete(0, END)
   get_audio_input.delete(0, END)

input_video_url = StringVar()
input_audio_url = StringVar()


def download(get_video_link=input_video_url.get() if input_video_url else None, get_audio_link=input_audio_url.get() if input_audio_url else None):

    video_link = input_video_url.get()
    audio_link = input_audio_url.get()

    if video_link:
        yt_video = YouTube(video_link)
        print('\nStart downloading... Please wait...\n')

        yvd = yt_video.streams.get_highest_resolution()
        yvd.download("C:\\Users\\Dejan\\Downloads\\Videos")

        print(f'\n{yt_video.title} Downloaded successfully')
        tkinter.messagebox.showinfo("Download finished", f"{yt_video.title} is saved on your pc")
        clear_text()


    if audio_link:
        yt_audio = YouTube(audio_link)
        print('\nStart downloading... Please wait...\n')

        yad = yt_audio.streams.filter(only_audio=True).first()
        out_file = yad.download("C:\\Users\\Dejan\\Downloads\\Audios")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(f'\n{yt_audio.title} Downloaded successfully')
        tkinter.messagebox.showinfo("Download finished", f"{yt_audio.title} is saved on your pc")
        clear_text()


    if 'https://www.youtube.com/' not in video_link and 'https://www.youtube.com/' not in audio_link:
        tkinter.messagebox.showinfo("File not found", "Choose video-url to download")
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
download_video_button = Button(root, width = 80, bg = 'green', fg = 'white', relief = 'sunken', text = 'Download',  command = download).pack()

#CLEAR FIELDS
Button(root, text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)



root.mainloop()
