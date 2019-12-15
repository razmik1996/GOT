#!/usr/bin/env python
from Tkinter import *
from PIL import Image, ImageTk
from player import *
from buildings import *
from soldier import *
from location import *
from pygame import mixer, time


def play_music():
    sound_file = "SoundFX/theme.mp3"
    # set volume from 0 to 1.0
    volume = 0.9
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment for good sound)
    mixer.init(freq, bitsize, channels, buffer)

    mixer.music.set_volume(volume)
    mixer.music.load(sound_file)
    mixer.music.play()

def exitfromgame():
    exit()

def show(event):
    canvas.pack(expand = YES, fill = BOTH)

def hide():
    canvas.pack_forget()

def settings():
    print "settings"

def play():

    mixer.music.stop()
    hide()

    
    canvasplay = Canvas(root, highlightthickness=0)
    canvasplay.pack(expand = YES, fill = BOTH)
    
    canvasplay.create_image(0, 0, image = imgBattlefield, anchor = NW)

    canvasLeft = Canvas(canvasplay)
    canvasRight = Canvas(canvasplay)

    canvasLeft.pack(side = LEFT)
    canvasRight.pack(side = RIGHT)



    
    #canvasplay.create_rectangle(0, 0, ws, hs)

    player1 = Player("1","Razmik",0,Country.ARMENIA,Color.BLUE, 1000)
    player2 = Player("2","Levon",0,Country.ENGLAND,Color.RED, 1000)
    location1 = Location(5,5)
    #FUNCTIONS FOR EVENTS_______________________________________
    def createArcherEvP1(event):
        createArcherP1()

    def createArcherEvP2(event):
        createArcherP2()
    
    def createSwordsmanEvP1(event):
        createSwordsmanP1()

    def createSwordsmanEvP2(event):
        createSwordsmanP2()

    def createMagEvP1(event):
        createMagP1()

    def createMagEvP2(event):
        createMagP2()
    #FUNCTIONS FOR EVENTS END___________________________________

    #FUNCTION SOLDERS__________________________________________
    listSoldersP1 = []
    listSoldersP2 = []

    def createArcherP1():
        if (player1.getMoney() >= 100):
            image_id1 = canvasplay.create_image(BuildLocalArcherP1.getX() * perPxlx, BuildLocalArcherP1.getY()*perPxly, image = imgArcherLeft)
            solder = Archer(player1, BuildLocalArcherP1, Direction.EAST, 100, 10, 2, 3, 100, image_id1)
            listSoldersP1.append(solder)
            player1.minusMoney(100)
        else:
            canvasplay.create_text(ws/2, hs/8, text = "Player1 don't have enough money you need 100 coin",\
                font = ('Impact', -25), fill = "grey")

    def createArcherP2():
        if (player2.getMoney() >= 100):
            image_id1 = canvasplay.create_image(BuildLocalArcherP2.getX() * perPxlx, BuildLocalArcherP2.getY()*perPxly, image = imgArcherRight)
            solder = Archer(player2, BuildLocalArcherP2, Direction.WEST, 100, 10, 2, 3, 100, image_id1)
            listSoldersP2.append(solder)
            player2.minusMoney(100)
        else:
            canvasplay.create_text(ws/2, 7*hs/8, text = "Player2 don't have enough money you need 100 coin",\
                font = ('Impact', -25), fill = "grey")

    def createSwordsmanP1():
        if (player1.getMoney() >= 200):
            image_id1 = canvasplay.create_image(BuildLocalSwordsmanP1.getX() * perPxlx, BuildLocalSwordsmanP1.getY()*perPxly, image = imgSwordsmanLeft)
            solder = Swordsman(player1, BuildLocalSwordsmanP1, Direction.EAST, 120, 15, 5, 1, 200, image_id1)
            listSoldersP1.append(solder)
            player1.minusMoney(200)
        else:
            canvasplay.create_text(ws/2, hs/8, text = "Player1 don't have enough money you need 200 coin",\
                font = ('Impact', -25), fill = "grey")

    def createSwordsmanP2():
        if (player2.getMoney() >= 200):
            image_id1 = canvasplay.create_image(BuildLocalSwordsmanP2.getX() * perPxlx, BuildLocalSwordsmanP2.getY()*perPxly, image = imgSwordsmanRight)
            solder = Swordsman(player2, BuildLocalSwordsmanP2, Direction.WEST, 120, 15, 5, 1, 200, image_id1)
            listSoldersP2.append(solder)
            player2.minusMoney(200)
        else:
            canvasplay.create_text(ws/2, 7*hs/8, text = "Player2 don't have enough money you need 200 coin",\
                font = ('Impact', -25), fill = "grey")

    def createMagP1():
        if (player1.getMoney() >= 300):
            image_id1 = canvasplay.create_image(BuildLocalMagP1.getX() * perPxlx, BuildLocalMagP1.getY()*perPxly, image = imgMagLeft)
            solder = Mag(player1, BuildLocalMagP1, Direction.EAST, 50, 25, 1, 2, 300, image_id1)
            listSoldersP1.append(solder)
            player1.minusMoney(300)
        else:
            canvasplay.create_text(ws/2, hs/8, text = "Player1 don't have enough money you need 300 coin",\
                font = ('Impact', -25), fill = "grey")

    def createMagP2():
        if (player2.getMoney() >= 300):
            image_id1 = canvasplay.create_image(BuildLocalMagP2.getX() * perPxlx, BuildLocalMagP2.getY()*perPxly, image = imgMagRight)
            solder = Mag(player2, BuildLocalMagP2, Direction.WEST, 50, 25, 1, 2, 300, image_id1)
            listSoldersP2.append(solder)
            player2.minusMoney(300)
        else:
            canvasplay.create_text(ws/2, 7*hs/8, text = "Player2 don't have enough money you need 300 coin",\
                font = ('Impact', -25), fill = "grey")
    #FUNCTION SOLDERS END______________________________________

    #BUTTONS________________________________________________
    archerSoldier1 = Button(canvasLeft, image = imgArcherLeft, command = createArcherP1)
    archerSoldier1.pack(side = TOP)

    swordsSoldier1 = Button(canvasLeft, image = imgSwordsmanLeft, command = createSwordsmanP1)
    swordsSoldier1.pack(side = TOP)

    magSoldier1 = Button(canvasLeft, image = imgMagLeft, command = createMagP1)
    magSoldier1.pack(side = TOP)

    archerSoldier2 = Button(canvasRight, image = imgArcherRight, command = createArcherP2)
    archerSoldier2.pack(side = TOP)

    swordsSoldier2 = Button(canvasRight, image = imgSwordsmanRight, command = createSwordsmanP2)
    swordsSoldier2.pack(side = TOP)

    magSoldier2 = Button(canvasRight, image = imgMagRight, command = createMagP2)
    magSoldier2.pack(side = TOP)
    #BUTTONSEND_______________________________________________

    #Build Buildings__________________________________________
    archerBuildingP1 = ArcherBuilding(player1, Location(random.randint(10,40),random.randint(35, 85)), 100,\
        10, 5, 20)
    BuildLocalArcherP1 = archerBuildingP1.getLocation()
    canvasplay.create_image(perPxlx * BuildLocalArcherP1.getX(), perPxly * BuildLocalArcherP1.getY(), image = imgBuildArcher, anchor=NW)

    archerBuildingP2 = ArcherBuilding(player2, Location(random.randint(60,90),random.randint(35, 85)), 100,\
        10, 5, 20)
    BuildLocalArcherP2 = archerBuildingP2.getLocation()
    canvasplay.create_image(perPxlx * BuildLocalArcherP2.getX(), perPxly * BuildLocalArcherP2.getY(), image = imgBuildArcher, anchor=NW)

    swordsmanBuildingP1 = SwordsmanBuilding(player1, Location(random.randint(10,40),random.randint(35, 85)), 100,\
        10, 5, 20)
    BuildLocalSwordsmanP1 = swordsmanBuildingP1.getLocation()
    locationFarSwToArchP1 = BuildLocalSwordsmanP1.getY() - BuildLocalArcherP1.getY()
    while(locationFarSwToArchP1 in range(-10, 10)):
        BuildLocalSwordsmanP1.setY(random.randint(35, 85))
        locationFarSwToArchP1 = BuildLocalSwordsmanP1.getY() - BuildLocalArcherP1.getY()
    canvasplay.create_image(perPxlx * BuildLocalSwordsmanP1.getX(), perPxly * BuildLocalSwordsmanP1.getY(), image = imgBuildSwordsman, anchor=NW)

    swordsmanBuildingP2 = SwordsmanBuilding(player2, Location(random.randint(60,90),random.randint(35, 85)), 100,\
        10, 5, 20)
    BuildLocalSwordsmanP2 = swordsmanBuildingP2.getLocation()
    locationFarSwToArchP2 = BuildLocalSwordsmanP2.getY() - BuildLocalArcherP2.getY()
    while(locationFarSwToArchP2 in range(-10, 10)):
        BuildLocalSwordsmanP2.setY(random.randint(35, 85))
        locationFarSwToArchP2 = BuildLocalSwordsmanP2.getY() - BuildLocalArcherP2.getY()
    canvasplay.create_image(perPxlx * BuildLocalSwordsmanP2.getX(), perPxly * BuildLocalSwordsmanP2.getY(), image = imgBuildSwordsman, anchor=NW)

    magBuildingP1 = MagBuilding(player1, Location(random.randint(10,40),random.randint(35, 85)), 100,\
        10, 5, 20)
    BuildLocalMagP1 = magBuildingP1.getLocation()
    while((BuildLocalMagP1.getY() - BuildLocalArcherP1.getY() <= 10) and (BuildLocalMagP1.getY() - BuildLocalArcherP1.getY() >= -10)):
        BuildLocalMagP1.setY(random.randint(35, 85))
    canvasplay.create_image(perPxlx * BuildLocalMagP1.getX(), perPxly * BuildLocalMagP1.getY(), image = imgBuildMag, anchor=NW)

    magBuildingP2 = MagBuilding(player2, Location(random.randint(60,90),random.randint(35, 85)), 100,\
        10, 5, 20)
    BuildLocalMagP2 = magBuildingP2.getLocation()
    while((BuildLocalMagP2.getY() - BuildLocalArcherP2.getY()) <= 5 and (BuildLocalMagP2.getY() - BuildLocalArcherP2.getY()) >= -5):
        BuildLocalMagP2.setY(random.randint(35, 85))
    canvasplay.create_image(perPxlx * BuildLocalMagP2.getX(), perPxly * BuildLocalMagP2.getY(), image = imgBuildMag, anchor=NW)
    
    global text_id1, text_id2

    def tickend():
        global text_id1, text_id2
        text_id1 = canvasplay.create_text(ws/6, hs/4, text = str(player1.getMoney()), font = ('Impact', -30), fill = "yellow")
        text_id2 = canvasplay.create_text(5 * ws/6, hs/4, text = str(player2.getMoney()), font = ('Impact', -30), fill = "yellow")
        call = root.after(100, tick)

    def tick():
        global text_id1, text_id2
        player1.getMoney()
        canvasplay.itemconfigure(text_id1, text = str(player1.getMoney()))
        canvasplay.itemconfigure(text_id2, text = str(player2.getMoney()))
        for i in range(0, len(listSoldersP1)):
            pass
        call = root.after(1000, tick)
    
    call = root.after(100, tickend)

    def dispShow(event):
        root.after_cancel(call)
        canvasplay.pack_forget()
        play_music()
        show(event)
        

    root.bind("<Escape>", dispShow)
    root.bind("<z>", createArcherEvP1)
    root.bind("<x>", createSwordsmanEvP1)
    root.bind("<c>", createMagEvP1)
    root.bind("<Left>", createArcherEvP2)
    root.bind("<Down>", createSwordsmanEvP2)
    root.bind("<Right>", createMagEvP2)

root = Tk()

play_music()

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


#BUTTONS IMAGE__________________________________________________
"""
imgPlayNormal = Image.open("Sprites/GUI/playNormalMenu.png")
imgPlayNormal = imgPlayNormal.resize((18 * perPxlx, int(25.5 * perPxly)))
imgPlayNormal = ImageTk.PhotoImage(imgPlayNormal)

imgSettingsNormal = Image.open("Sprites/GUI/settingsNormalMenu.png")
imgSettingsNormal = imgSettingsNormal.resize((18 * perPxlx, int(25.5 * perPxly)))
imgSettingsNormal = ImageTk.PhotoImage(imgSettingsNormal)

imgQuitNormal = Image.open("Sprites/GUI/quitNormalMenu.png")
imgQuitNormal = imgQuitNormal.resize((18 * perPxlx, int(25.5 * perPxly)))
imgQuitNormal = ImageTk.PhotoImage(imgQuitNormal)
"""
imgPlayNormal = Image.open("Sprites/GUI/playNormalMenu.png")
imgPlayNormal = imgPlayNormal.resize((ws/6, int(hs/4.21875)))
imgPlayNormal = ImageTk.PhotoImage(imgPlayNormal)

imgSettingsNormal = Image.open("Sprites/GUI/settingsNormalMenu.png")
imgSettingsNormal = imgSettingsNormal.resize((ws/6, int(hs/4.21875)))
imgSettingsNormal = ImageTk.PhotoImage(imgSettingsNormal)

imgQuitNormal = Image.open("Sprites/GUI/quitNormalMenu.png")
imgQuitNormal = imgQuitNormal.resize((ws/6, int(hs/4.21875)))
imgQuitNormal = ImageTk.PhotoImage(imgQuitNormal)
#BUTTONS IMAGE END________________________________________________

imgBattlefield = Image.open("Sprites/battlefield.png")
imgBattlefield = imgBattlefield.resize((ws, hs))
imgBattlefield = ImageTk.PhotoImage(imgBattlefield)
    

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