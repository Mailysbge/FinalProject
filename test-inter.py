from tkinter import *
from random import randint, shuffle

fenetre = Tk()
fenetre.title('Jeu1')
fenetre.geometry('300x300+400+400')

fenetre2 = Tk()
fenetre2.title('Jeu2')
fenetre.geometry('200x200+100+100')

# Fonction qui affiche la fenetre d'un mini jeu
def OpenFenetre():
    fenetre.mainloop()

def OpenFenetre2():
    fenetre2.mainloop()


# Création de la fenêtre principale (main window)
Mafenetre = Tk()

Mafenetre.title('Arena games')
Mafenetre.geometry('600x600+400+400')

# Création d'un widget Button (bouton mémorie)
Jeu1 = Button(Mafenetre, text ='Memory', command = OpenFenetre)
# Positionnement du widget avec la méthode pack()
Jeu1.pack(side = LEFT, padx = 140, pady = 150)

# Création d'un widget Button (bouton Ping-pong)
Jeu2 = Button(Mafenetre, text ='Ping-Pong', command = OpenFenetre2)
Jeu2.pack(side = LEFT, padx = 100, pady = 150)
Texte = StringVar()

Mafenetre.mainloop()