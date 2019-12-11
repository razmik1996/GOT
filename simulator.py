from Tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

botFrame = Frame(root)
botFrame.pack(side = BOTTOM)

Button1 = Button(topFrame, text = "Start",fg = "Red")
Button1.pack(side=LEFT)

Button2 = Button(topFrame, text = "Load",fg = "Blue")
Button2.pack(side=LEFT)

Button3 = Button(botFrame, text = "Settings",fg = "Green")
Button3.pack(side=LEFT)

Button4 = Button(botFrame, text = "Quit",fg = "Black")
Button4.pack(side=LEFT)

root.mainloop()