#!/usr/bin/env python
from Tkinter import *
from PIL import Image, ImageTk

def exitfromgame():
    exit()

root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

print ws, hs

root.attributes("-fullscreen", True)
canvas = Canvas(root)
root.title("Game Of Thrones")
canvas.pack(expand = YES, fill = BOTH)

frame = Frame(root, bg = None)

backgroundImage = Image.open("Sprites/Background.png")
backgroundImage = backgroundImage.resize((ws, hs))
backgroundImage = ImageTk.PhotoImage(backgroundImage)
canvas.create_image(0, 0, image = backgroundImage, anchor = NW)
canvas.create_window(ws/2 + ws/6, hs/2, window = frame, width = ws/6, height = 5*hs/6)


Button1 = Button(frame, text = "Start",fg = "Red")
Button1.pack(ipadx = 50, ipady = 50, padx = 300, pady = 100)

Button2 = Button(frame, text = "Load",fg = "Blue")
Button2.pack(ipadx = 50, ipady = 50, padx = 360, pady = 160)

Button3 = Button(frame, text = "Settings",fg = "Green")
Button3.pack(ipadx = 50, ipady = 50, padx = 380, pady = 220)

Button4 = Button(frame, text = "Quit",fg = "Black", command = exitfromgame)
Button4.pack(padx = 1, pady = 1)


root.mainloop()
