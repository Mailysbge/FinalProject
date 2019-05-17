import tkinter
import pygame
from tkinter import *
from views.Menu import Menu
from views.MemoryBase import MemoryBase
from morpion.Morpion import Morpion
from pingPong.PingPong import PingPong


def removeAllFrames():
    global CurrentFrame
    if (CurrentFrame is not None):
        CurrentFrame.destroy()
        emptyMenu = tkinter.Menu(master)
        master.config(menu=emptyMenu)
        if (pygame.mixer.get_init() is not None):
            pygame.mixer.stop()


def showMemory():
    global CurrentFrame
    removeAllFrames()
    master.title("Memory")
    CurrentFrame = MemoryBase().createFrame(master, showMenu)


def showPingPong():
    global CurrentFrame
    removeAllFrames()
    master.title("Ping-Pong")
    CurrentFrame = PingPong().createFrame(master, showMenu)


def showMorpion():
    global CurrentFrame
    removeAllFrames()
    master.title("Morpion")
    CurrentFrame = Morpion().createFrame(master, showMenu)


def showMenu():
    global CurrentFrame
    removeAllFrames()
    master.title('Arena games')
    CurrentFrame = Menu().createFrame(master, showMemory, showPingPong, showMorpion)


# Programme principal
master = tkinter.Tk()
CurrentFrame = None
showMenu()
tkinter.mainloop()
