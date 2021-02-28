from tkinter import Label, Entry, Button, StringVar, filedialog, messagebox, Tk
from pytube import YouTube
  
def Widgets(): 
    link_label = Label(window,  text="YouTube link:", bg="gainsboro") 
    link_label.grid(row=1, column=0, pady=5, padx=5) 
   
    window.linkText = Entry(window, width=55, textvariable=video_Link) 
    window.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2) 
   
    destination_label = Label(window, text="Destination:", bg="gainsboro") 
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
    download_Folder = download_Path.get()
    try:
        getVideo = YouTube(Youtube_link)
    except:
        messagebox.showerror("Error","No Internet Connection!")
    else:
        videoStream = getVideo.streams.get_highest_resolution() 
        videoStream.download(download_Folder) 
        messagebox.showinfo("SUCCESSFUL!", f"DOWNLOADED AND SAVED IN\n {download_Folder}") 
  

window = Tk() 
window.geometry("470x110") 
window.resizable(False, False) 
window.title("YouTube_Video_Downloader") 
window.config(background="gainsboro") 
   

video_Link = StringVar() 
download_Path = StringVar() 
   
Widgets() 
   
window.mainloop() 
