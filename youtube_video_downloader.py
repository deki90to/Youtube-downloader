from tkinter import *
import tkinter.messagebox
from pytube import YouTube
from sys import argv


root = Tk()
root.geometry('400x100')
root['bg']='#004038'
root.title('Convertor to MP4')


def clear_text():
   convert_entry.delete(0, END)


input_value = StringVar()

def video_download(get_link = input_value.get()):

    link = input_value.get()

    if not link or 'youtube' not in link:
        tkinter.messagebox.showinfo("File not found", "Choose video-url to download")
        clear_text()
    else:
        yt = YouTube(link)

        print('Start downloading... Please wait...\n')
        print(f"Title {yt.title}")

        yd = yt.streams.get_highest_resolution()
        yd.download("C:\\Users\\Dejan\\Downloads")

        print('\nDownload finished')
        tkinter.messagebox.showinfo("Download finished", "Video is saved on your pc")
        clear_text()


label = Label(root, text = 'YT Video Downloader', bg = '#004038', fg = 'white')
label.pack()

convert_entry = Entry(root, width = 100, textvar = input_value)
convert_entry.pack()

download_button = Button(root, width = 80, bg = 'green', fg = 'white', relief = 'sunken', text = 'Download',  command = video_download)
download_button.pack()

Button(root, text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)


root.mainloop()