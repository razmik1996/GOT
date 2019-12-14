#!/usr/bin/env python
from Tkinter import *
from PIL import Image, ImageTk
from player import *
from buildings import ArcherBuilding
from soldier import *



def exitfromgame():
    exit()

def show(event):
    canvas.pack(expand = YES, fill = BOTH)

def hide():
    canvas.pack_forget()

def play():
    hide()
    canvasplay = Canvas(root)
    canvasplay.pack(expand = YES, fill = BOTH)
    canvasLeft = Canvas(canvasplay)
    canvasRight = Canvas(canvasplay)

    canvasLeft.pack(side = LEFT)
    canvasRight.pack(side = RIGHT)

    canvasplay.create_rectangle(0, 0, ws, hs, fill="#ccffcc")

    player1 = Player("1","Razmik",0,Country.ARMENIA,Color.BLUE)
    player2 = Player("2","Levon",0,Country.ENGLAND,Color.RED)

    location1 = Location(5,5)

    archerBuild1 = Button(canvasLeft, image = imgArcherLeft)
    archerBuild1.pack(side = TOP)

    swordsBuild1 = Button(canvasLeft, image = imgSwordsmanLeft)
    swordsBuild1.pack(side = TOP)

    magBuild1 = Button(canvasLeft, image = imgMagLeft)
    magBuild1.pack(side = TOP)

    archerBuild2 = Button(canvasRight, image = imgArcherRight)
    archerBuild2.pack(side = TOP)

    swordsBuild2 = Button(canvasRight, image = imgSwordsmanRight)
    swordsBuild2.pack(side = TOP)

    magBuild2 = Button(canvasRight, image = imgMagRight)
    magBuild2.pack(side = TOP)

    def dispShow(event):
        canvasplay.pack_forget()
        show(event)

    root.bind("<Escape>", dispShow)

root = Tk()


imgArcher = PhotoImage(file = "Sprites/Enemy1/Idle/Idle_000.png")
imgArcherLeft = imgArcher.subsample(5, 5)
imgArcherRight = imgArcher.subsample(-5, 5)

imgSwordsman = PhotoImage(file = "Sprites/Enemy3/Idle/Idle_000.png")
imgSwordsmanLeft = imgSwordsman.subsample(5, 5)
imgSwordsmanRight = imgSwordsman.subsample(-5, 5)

imgMag = PhotoImage(file = "Sprites/Enemy2/Idle/Idle_000.png")
imgMagLeft = imgMag.subsample(5, 5)
imgMagRight = imgMag.subsample(-5, 5)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
perPxlx = ws/100
perPxly = hs/100

print ws, hs

root.attributes("-fullscreen", True)
canvas = Canvas(root, border = 0)
root.title("Game Of Thrones")
canvas.pack(expand = YES, fill = BOTH)

canvasInner = Canvas(canvas, border = 0, borderwidth = 0)

#frameBg = Image.open("Sprites/GUI/button.png")
#frameBg = frameBg.resize((ws, hs))
#frameBg = ImageTk.PhotoImage(frameBg)

backgroundImage = Image.open("Sprites/Background.png")
backgroundImage = backgroundImage.resize((ws, hs))
backgroundImage = ImageTk.PhotoImage(backgroundImage)
canvas.create_image(0, 0, image = backgroundImage, anchor = NW)
#canvasInner.create_image(0, 0, image = frameBg, anchor = NW)
canvas.create_window(ws/2 + ws/6, hs/2, window = canvasInner, width = ws/6, height = 14*hs/20)

imgPlayNormal = Image.open("Sprites/GUI/playNormal.png")
imgPlayNormal = imgPlayNormal.resize((17 * perPxlx, 25 * perPxly))
imgPlayNormal = ImageTk.PhotoImage(imgPlayNormal)
imgPlayHower = PhotoImage(file = "Sprites/GUI/playHower.png")
imgPlayHower = imgPlayHower.subsample(3, 5)

imgSettingsNormal = Image.open("Sprites/GUI/settingsNormal.png")
imgSettingsNormal = imgSettingsNormal.resize((17 * perPxlx, 25 * perPxly))
imgSettingsNormal = ImageTk.PhotoImage(imgSettingsNormal)
imgSettingsHower = PhotoImage(file = "Sprites/GUI/settingsHover.png")
imgSettingsHower = imgSettingsHower.subsample(3, 5)

imgQuitNormal = Image.open("Sprites/GUI/quitNormal.png")
imgQuitNormal = imgQuitNormal.resize((17 * perPxlx, 25 * perPxly))
imgQuitNormal = ImageTk.PhotoImage(imgQuitNormal)
imgQuitHower = PhotoImage(file = "Sprites/GUI/quitHover.png")
imgQuitHower = imgQuitHower.subsample(3, 5)

Button1 = Button(canvasInner, image = imgPlayNormal, border =0, command = play)
Button1.pack(side = TOP)

Button2 = Button(canvasInner, image = imgSettingsNormal, border=0)
Button2.pack(side = TOP)

Button3 = Button(canvasInner, image = imgQuitNormal, borderwidth=0, command = exitfromgame)
Button3.pack(side = TOP)

root.mainloop()
