#!/usr/bin/env python
from Tkinter import *
from PIL import Image, ImageTk
from player import *
from buildings import *
from soldier import *
from location import *

def exitfromgame():
    exit()

def show(event):
    canvas.pack(expand = YES, fill = BOTH)

def hide():
    canvas.pack_forget()

def settings():
    print "settings"

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

    #BUTTONS________________________________________________
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
    #BUTTONSEND_______________________________________________

    #Build Buildings__________________________________________
    archerBuildingP1 = ArcherBuilding(player1, Location(random.randint(10,40),random.randint(0, 100)), 100,\
        10, 5, 20)
    BuildLocal = archerBuildingP1.getLocation()
    canvasplay.create_image(perPxlx * BuildLocal.getX(), perPxly * BuildLocal.getY(), image = imgBuildArcher, anchor=NW)

    archerBuildingP2 = ArcherBuilding(player2, Location(random.randint(60,90),random.randint(0, 100)), 100,\
        10, 5, 20)
    BuildLocal = archerBuildingP2.getLocation()
    canvasplay.create_image(perPxlx * BuildLocal.getX(), perPxly * BuildLocal.getY(), image = imgBuildArcher, anchor=NW)

    swordsmanBuildingP1 = SwordsmanBuilding(player1, Location(random.randint(10,40),random.randint(0, 100)), 100,\
        10, 5, 20)
    BuildLocal = swordsmanBuildingP1.getLocation()
    canvasplay.create_image(perPxlx * BuildLocal.getX(), perPxly * BuildLocal.getY(), image = imgBuildSwordsman, anchor=NW)

    swordsmanBuildingP2 = SwordsmanBuilding(player2, Location(random.randint(60,90),random.randint(0, 100)), 100,\
        10, 5, 20)
    BuildLocal = swordsmanBuildingP2.getLocation()
    canvasplay.create_image(perPxlx * BuildLocal.getX(), perPxly * BuildLocal.getY(), image = imgBuildSwordsman, anchor=NW)

    magBuildingP1 = MagBuilding(player1, Location(random.randint(10,40),random.randint(0, 100)), 100,\
        10, 5, 20)
    BuildLocal = magBuildingP1.getLocation()
    canvasplay.create_image(perPxlx * BuildLocal.getX(), perPxly * BuildLocal.getY(), image = imgBuildMag, anchor=NW)

    magBuildingP2 = MagBuilding(player2, Location(random.randint(60,90),random.randint(0, 100)), 100,\
        10, 5, 20)
    BuildLocal = magBuildingP2.getLocation()
    canvasplay.create_image(perPxlx * BuildLocal.getX(), perPxly * BuildLocal.getY(), image = imgBuildMag, anchor=NW)

    def dispShow(event):
        canvasplay.pack_forget()
        show(event)

    root.bind("<Escape>", dispShow)

root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
perPxlx = ws/100
perPxly = hs/100

#BUILDINGS IMAGES OPENING____________________________________________
imgBuildArcher = Image.open("Sprites/Towers/ArcherTower.png")
imgBuildArcher = imgBuildArcher.resize((8 * perPxlx, 13 * perPxly))
imgBuildArcher = ImageTk.PhotoImage(imgBuildArcher)

imgBuildSwordsman = Image.open("Sprites/Towers/Tower2.png")
imgBuildSwordsman = imgBuildSwordsman.resize((8 * perPxlx, 13 * perPxly))
imgBuildSwordsman = ImageTk.PhotoImage(imgBuildSwordsman)

imgBuildMag = Image.open("Sprites/Towers/Tower3.png")
imgBuildMag = imgBuildMag.resize((8 * perPxlx, 13 * perPxly))
imgBuildMag = ImageTk.PhotoImage(imgBuildMag)
#END BULD IMAGES_____________________________________________________
#SOLDER IMAGES OPENING________________________________________________
imgArcher = PhotoImage(file = "Sprites/Enemy1/Idle/Idle_000.png")
imgArcherLeft = imgArcher.subsample(5, 5)
imgArcherRight = imgArcher.subsample(-5, 5)

imgSwordsman = PhotoImage(file = "Sprites/Enemy3/Idle/Idle_000.png")
imgSwordsmanLeft = imgSwordsman.subsample(5, 5)
imgSwordsmanRight = imgSwordsman.subsample(-5, 5)

imgMag = PhotoImage(file = "Sprites/Enemy2/Idle/Idle_000.png")
imgMagLeft = imgMag.subsample(5, 5)
imgMagRight = imgMag.subsample(-5, 5)

root.attributes("-fullscreen", True)
canvas = Canvas(root, border = 0, highlightthickness = 0)
root.title("Game Of Thrones")
canvas.pack(expand = YES, fill = BOTH)

canvasInner = Canvas(canvas,highlightthickness=0, border = 0, borderwidth = 0)

#frameBg = Image.open("Sprites/GUI/button.png")
#frameBg = frameBg.resize((ws, hs))
#frameBg = ImageTk.PhotoImage(frameBg)

backgroundImage = Image.open("Sprites/Background.png")
backgroundImage = backgroundImage.resize((ws, hs))
backgroundImage = ImageTk.PhotoImage(backgroundImage)
canvas.create_image(0, 0, image = backgroundImage, anchor = NW)
#canvasInner.create_image(0, 0, image = frameBg, anchor = NW)
canvas.create_window(ws/2 + ws/6, hs/2, window = canvasInner, width = ws/6, height = 14*hs/20)



imgPlayNormal = PhotoImage(file = "Sprites/GUI/playNormalMenu.png")
imgSettingsNormal = PhotoImage(file = "Sprites/GUI/settingsNormalMenu.png")
imgQuitNormal = PhotoImage(file = "Sprites/GUI/quitNormalMenu.png")

Button1 = Button(canvasInner, activebackground = '#101110',
                bg = '#101110', highlightthickness = 0,
                image = imgPlayNormal, border = 0, 
                borderwidth = 0, command = play).pack(side = TOP)

Button2 = Button(canvasInner, activebackground = '#2b2d2f', 
                bg = '#2b2d2f', highlightthickness = 0, 
                image = imgSettingsNormal, border = 0, 
                borderwidth = 0, command = settings).pack(side = TOP)

Button3 = Button(canvasInner,activebackground = '#2b2d2f',
                bg = '#2b2d2f',highlightthickness = 0, 
                image = imgQuitNormal, border = 0,
                borderwidth = 0, command = exitfromgame).pack(side = TOP)


'''
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

Button2 = Button(canvasInner, image = imgSettingsNormal, border=0)
Button2.pack(side = TOP)

'''

root.mainloop()
