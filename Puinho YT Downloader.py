#import
import imp
from tkinter import *
from turtle import width
from pytube import *
from tkinter import filedialog

#configuração da janela
screen = Tk()
title = screen.title("Puinho YT Downloader")
canvas = Canvas(screen, width = 500, height = 300)
canvas.pack()

#recursos

logo = PhotoImage(file = "yt_img.png")
logo = logo.subsample(3, 3)
canvas.create_image(250, 80, image = logo)

label = Label(text = "Insira o link de download")
label.place(x= 185, y = 160)

link = Entry(screen, width= 50)
link.place(x= 100, y = 200)

def download_file():
    vd = link.get()
    savein = filedialog.askdirectory()
    yt = YouTube(vd).streams.get_highest_resolution().download(savein)
    print("Título: ", YouTube.title)

button = Button(text = "Donwload", command=download_file)
button.place(x = 217, y = 260)

#exit
screen.mainloop()