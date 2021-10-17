import os
# from posixpath import expanduser
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

location = os.path.join(os.path.expanduser('~'),'Download')

def download_mp3(url, lb1):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        downloaded_video = video.download(location)
        base, ext = os.path.splitext(downloaded_video)
        new_file = base + 'mp3'
        os.rename(downloaded_video,new_file)
        lb1.config(text='Succes', font=('Arial',14), fg="green")
    except:
        error_message()
        lb1.config(text='Error', font=('Arial',14), fg="red")
      
def open_downloads():
    os.startfile(location)

def delete_txtbox(tb1):
    tb1.delete(0,END)

def error_message():
    messagebox.showinfo('Error','Invalid link!')    
