import tkinter
import pygame
from tkinter import *
from interfaceAccueil.Menu import Menu
from memory.MemoryBase import MemoryBase
from morpion.Morpion import Morpion
from pingPong.PingPong import PingPong

def removeAllFrames():
    """Fonction qui permet de supprimer touts les cadres du menu pour lancé
    juste le jeu """
    global FRAME
    if (FRAME is not None):
        FRAME.destroy()
        emptyMenu = tkinter.Menu(master)
        master.config(menu=emptyMenu)
        if (pygame.mixer.get_init() is not None):
            pygame.mixer.stop()


def showMemory():
    """Fonction qui permet d'aficher le memory"""
    global FRAME
    removeAllFrames()
    master.title("Memory")
    FRAME = MemoryBase().createFrame(master, showMenu)


def showPingPong():
    """Fonction qui permet d'aficher le PingPong"""
    global FRAME
    removeAllFrames()
    master.title("Ping-Pong")
    FRAME = PingPong().createFrame(master, showMenu)


def showMorpion():
    """Fonction qui permet d'aficher le Morpion"""
    global FRAME
    removeAllFrames()
    master.title("Morpion")
    FRAME = Morpion().createFrame(master, showMenu)


def showMenu():
    """Fonction qui permet d'aficher l'interface d'acceuil"""
    global FRAME
    removeAllFrames()
    master.title('Arena games')
    FRAME = Menu().createFrame(master, showMemory, showPingPong,
     showMorpion)

def onClosing():
    if (pygame.mixer.get_init() is not None):
        pygame.mixer.stop()
    master.destroy()

# Programme principal
master = tkinter.Tk()
master.protocol("WM_DELETE_WINDOW", onClosing)
FRAME = None
showMenu()
tkinter.mainloop()
