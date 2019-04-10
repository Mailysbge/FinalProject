from tkinter import *


def createFrame(window, callbackButtonClick):
    frame = Frame(window)
    b = Button(frame, text="Go to jeux", command=callbackButtonClick).pack()
    return frame

def createFrame2(window, callbackButtonClick):
    frame2 = Frame(window)
    b2 = Button(frame, text="Go to jeux 2", command=callbackButtonClick).pack()
    return frame
