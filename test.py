from tkinter import *
from threading import Thread

class LastChance(Thread):
    def __init__(self, nom):
        Thread.__init__(self, name = nom)
    def run(self):
        traitement()

a = LastChance('A')
b = LastChance('B')
fenetre = Tk()
Jeu1 = Button(fenetre, text ='Test', command = a.start)
Jeu2 = Button(fenetre, text ='Test2', command = b.start)

fenetre.geometry('600x600+300+200')
Jeu1.pack(side = LEFT, padx = 140, pady = 150)
Jeu2.pack(side = LEFT, padx = 100, pady = 150)


def traitement():
    fen2 = Tk()
    fen2.mainloop()

fenetre.mainloop()

