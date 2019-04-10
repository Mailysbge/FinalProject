from tkinter import *
from random import randint, shuffle
import frames.Menu as Menu
import frames.Jeux as Jeux

def Manga():
    print('Hello')

def dan():
    print('Good game')

def callbackMenu():
    MenuFrame.pack_forget()
    JeuxFrame.pack()


def callbackJeux():
    JeuxFrame.pack_forget()
    JeuxFrame2.pack()


def callbackJeux2():
    JeuxFrame2.pack_forget()
    MenuFrame.pack()


# Création de la fenêtre principale (main window)
Mafenetre = Tk()

Mafenetre.title('Arena games')
Mafenetre.geometry('600x700+600+100')


MenuFrame = Menu.createFrame(master, callbackMenu)
JeuxFrame = Jeux.createFrame(master, callbackJeux)

JeuxFrame2 = Jeux.createFrame(
    master, callbackMenu, "Go back to the menu now !")

JeuxFrame3 = Jeux.createFrame(
    master, callbackMenu, "Retour")

MenuFrame.pack()
mainloop()

# Création d'un widget Button (bouton mémorie)
#Jeu1 = Button(Mafenetre, text ='Memory', command = Manga)
# Positionnement du widget avec la méthode pack()
#Jeu1.pack(side = LEFT, padx = 140, pady = 150)

# Création d'un widget Button (bouton Ping-pong)
#Jeu2 = Button(Mafenetre, text ='Ping-Pong', command = dan)
#Jeu2.pack(side = LEFT, padx = 100, pady = 150)
#Texte = StringVar()
#Manga()

#Mafenetre.mainloop()