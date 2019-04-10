from tkinter import *
import frames.Menu as Menu
import frames.Jeux as Jeux


def callbackMenu():
    MenuFrame.pack_forget()
    JeuxFrame.pack()


def callbackJeux():
    JeuxFrame.pack_forget()
    JeuxFrame2.pack()


def callbackJeux2():
    JeuxFrame2.pack_forget()
    MenuFrame.pack()

def callbackJeux3():
    JeuxFrame3.pack_forget()
    MenuFrame.pack()

master = Tk()
master.title('Arena games')
master.geometry('600x300+200+400')

MenuFrame = Menu.createFrame(master, callbackMenu)

JeuxFrame = Jeux.createFrame(master, callbackJeux)

JeuxFrame2 = Jeux.createFrame(
    master, callbackMenu, "Go back to the menu now !")

JeuxFrame3 = Jeux.createFrame(
    master, callbackMenu, "Retour")

MenuFrame.pack()
mainloop()
