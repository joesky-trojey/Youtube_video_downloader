import tkinter as tk
from tkinter import filedialog 
import os
from PIL import Image, ImageTk
import yt_dlp



def download():
    try:
        info_lable=tk.Label(downloader_app, text=f"Downloading....", foreground="yellow")
        info_lable.grid(row=4, column=0, pady=(10, 70))
        ydl_opts={
            'outtmpl': '~/Downloads/%(title)s.%(ext)s',  # Specify the output file name and location
        }
        link=link_input.get()

        ydl_opts = {}
       

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # info=ydl.extract_info(link, download=False)

            ydl.download([link])
        
        success_label=tk.Label(downloader_app, text=f"Successifully downloaded Your video", background="yellow", foreground='green')

        success_label.grid(row=5, column=0, pady=(10, 60))
 
    except Exception as e:
        error_label=tk.Label(downloader_app, text=f"An Error occured while trying to downloda the video {str(e)}", background="cyan", foreground='red')

        error_label.grid(row=4, column=0, pady=(10, 70))


#create the downloader app object
downloader_app=tk.Tk()
downloader_app.geometry("700x400")
downloader_app.resizable(0,0)
downloader_app.title("Youtube Video Downloader")
downloader_app.update_idletasks()

app_width=downloader_app.winfo_width()
app_height=downloader_app.winfo_height()

background="bg1.jpg"
app_background_temp=Image.open(background)
app_background_temp=app_background_temp.resize((app_width, app_height))
bg_img=ImageTk.PhotoImage(app_background_temp)
background=tk.Label(downloader_app, image=bg_img)
background.place(relheight=1,relwidth=1)

link_input_lable=tk.Label(downloader_app, text="Enter link to youtube video")
link_input_lable.config(background='cyan')
link_input_lable.grid(row=0, column=0, padx=250, pady=(80, 0), )

link_input=tk.Entry(downloader_app)
link_input.grid(row=1, column=0, padx=10, pady=10)

download_btn=tk.Button(downloader_app, text="Download", command=download)
download_btn.config(background='cyan')
download_btn.grid(row=3, column=0, padx=0, pady=0)



downloader_app.mainloop()