#!/usr/bin/env python
from Tkinter import *
from PIL import Image, ImageTk

def exitfromgame():
    exit()

root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

root.attributes("-fullscreen", True)
canvas = Canvas(root)
root.title("Game Of Thrones")
canvas.pack(expand = YES, fill = BOTH)

frame = Frame(root, bg = None)

backgroundImage = Image.open("Sprites/Background.png")
backgroundImage = backgroundImage.resize((ws, hs))
backgroundImage = ImageTk.PhotoImage(backgroundImage)
canvas.create_image(0, 0, image = backgroundImage, anchor = NW)
canvas.create_window(ws/2 + 250, hs/2, window = frame, width = 300, height = 800)


Button1 = Button(canvas, text = "Start",fg = "Red")
Button1.pack(ipadx = 50, ipady = 50, padx = 300, pady = 100)

Button2 = Button(canvas, text = "Load",fg = "Blue")
Button2.pack(ipadx = 50, ipady = 50, padx = 360, pady = 160)

Button3 = Button(canvas, text = "Settings",fg = "Green")
Button3.pack(ipadx = 50, ipady = 50, padx = 380, pady = 220)

Button4 = Button(canvas, text = "Quit",fg = "Black", command = exitfromgame)
Button4.pack(padx = 1, pady = 1)


root.mainloop()
