#you need to have FFmpeg to be able to use this.

from tkinter import Label, Entry, Button, StringVar, filedialog, messagebox, Tk
from youtube_dl import YoutubeDL
import subprocess
  
def Widgets(): 
    link_label = Label(window,  text="YouTube link:", bg="peach puff") 
    link_label.grid(row=1, column=0, pady=5, padx=5) 
   
    window.linkText = Entry(window, width=55, textvariable=video_Link) 
    window.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2) 
   
    destination_label = Label(window, text="Destination:", bg="peach puff") 
    destination_label.grid(row=2, column=0, pady=5, padx=5) 
   
    window.destinationText = Entry(window, width=40, textvariable=download_Path) 
    window.destinationText.grid(row=2, column=1, pady=5, padx=5) 
   
    browse_button = Button(window, text="Browse", command=BrowseDirectory, width=10, bg="LightCyan2") 
    browse_button.grid(row=2, column=2, pady=1, padx=1) 
   
    download_button = Button(window, text="Download", command=DownloadVideo, width=20, bg="LightCyan2") 
    download_button.grid(row=3, column=1, pady=5, padx=3) 
  
  
def BrowseDirectory():
    """Browses the folders to save the file."""
    download_path = filedialog.askdirectory(initialdir="C:") 
   
    download_Path.set(download_path) 
  
  
def DownloadVideo(): 
    """Downloads the video from the link."""
    Youtube_link = video_Link.get()
    video_info = YoutubeDL().extract_info(url= Youtube_link, download=False)
    download_Folder = download_Path.get()
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f"{download_Folder}/{filename}",
        'postprocessors':[{
            "key": "FFmpegExtractAudio",
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    subprocess.call("open", filename)


window = Tk() 
window.geometry("470x110") 
window.resizable(False, False) 
window.title("YouTube mp3 Downloader") 
window.config(background="peach puff") 
   

video_Link = StringVar() 
download_Path = StringVar() 
   
Widgets() 
   
window.mainloop() 
