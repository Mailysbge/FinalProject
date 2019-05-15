import tkinter
from tkinter import *
from views.Menu import Menu
from views.MemoryBase import MemoryBase
from jeuPing.DanDu import DanDu

def removeAllFrames():
    global CurrentFrame
    if (CurrentFrame is not None):
        CurrentFrame.destroy()
        emptyMenu = tkinter.Menu(master)
        master.config(menu=emptyMenu)

def showMemory():
    global CurrentFrame
    removeAllFrames()
    master.title("Memory")
    CurrentFrame = MemoryBase().createFrame(master, showMenu)

def showPingPong():
    global CurrentFrame
    removeAllFrames()
    master.title("Ping-Pong")
    CurrentFrame = DanDu().createFrame(master, showMenu)

def showMenu():
    global CurrentFrame
    removeAllFrames()
    master.title('Arena games')
    CurrentFrame = Menu().createFrame(master, showMemory, showPingPong)

# Programme principal
master = tkinter.Tk()
CurrentFrame = None
showMenu()
tkinter.mainloop()