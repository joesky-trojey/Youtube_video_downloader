import tkinter as tk
from tkinter import filedialog 
import os
from PIL import Image, ImageTk

#create the downloader app object
downloader_app=tk.Tk()
downloader_app.geometry=("700x400")
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

downloader_app.mainloop()