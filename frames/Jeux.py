from tkinter import *


def createFrame(window, callbackButtonClick, buttonText="Go jeu 2"):
    frame = Frame(window)
    b2 = Button(frame, text=buttonText,
                command=callbackButtonClick).pack()
    return frame
