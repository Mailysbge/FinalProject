from tkinter import *
import pygame
import random
import math
from PIL import Image, ImageTk
Largeur = 1024 # en pixels
Hauteur = 700

Mafenetre = Tk()
lbScore1 = Label(Mafenetre, text="")
lbScore2 = Label(Mafenetre, text="")
score_1 = 0
score_2 = 0

R1X = 0
R1Y = 0
R2X = 0
R2Y = 0

RHauteur = 160
RLargeur = 5

class Game:
    #Musique du jeu
    pygame.mixer.init()
    pygame.mixer.Sound("jeuPing/ping-pong-song.wav").play(-1)

Rayon = 7 # rayon de la balle

# position initiale au milieu
X = Largeur/2
Y = Hauteur/2

# direction initiale aléatoire
vitesse = random.uniform(1.8, 2)*5
angle = random.uniform(0, 2*math.pi)
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)


def deplacement_balle():

    """ Déplacement de la balle """
    global X,Y,DX,DY,Rayon,Largeur,Hauteur,RX1,RY1,RX2,RY2,RHauteur,RLargeur,score_1,score_2,lbScore1

    # rebond à droite
    if X+Rayon+DX > Largeur:
        score_1 += 1
        lbScore1['text'] = "Joueur 1 : " + format(str(score_1))
        X = Largeur / 2
        Y = Hauteur / 2
        DX = vitesse*math.cos(angle)
        DY = vitesse*math.sin(angle)

    # rebond à gauche
    if X-Rayon+DX < 0:
        score_2 += 1
        lbScore2['text'] = "Joueur 2 : " + format(str(score_2))
        X = Largeur / 2
        Y = Hauteur / 2
        DX = vitesse*math.cos(angle)
        DY = vitesse*math.sin(angle)

    # rebond en bas
    if Y+Rayon+DY > Hauteur:
        Y = 2*(Hauteur-Rayon)-Y
        DY = -DY

    # rebond en haut
    if Y-Rayon+DY < 0:
        Y = 2*Rayon-Y
        DY = -DY

    # Rebond raquette 1
    if (Y+DY > R1Y - RHauteur/2) and (Y+DY < R1Y + RHauteur/2):
        if (X+DX > R1X):
            DX = -DX

    # Rebond raquette 2
    if (Y+DY > R2Y - RHauteur/2) and (Y+DY < R2Y + RHauteur/2):
        if (X+DX < R2X+RLargeur):
            DX = -DX

    X = X+DX
    Y = Y+DY

    # affichage
    MonCanevas.coords(Balle, X-Rayon,
     Y-Rayon, X+Rayon, Y+Rayon)

    # mise à jour toutes les 50 ms
    Mafenetre.after(50, deplacement_balle)

def haut1(event):
    global R1Y
    """mouvement vers le haut de la raquette 1"""
    R1Y = R1Y - 10
    if (R1Y-RHauteur/2) < 0 :
        R1Y = R1Y + 10
    else :
        MonCanevas.move(Raquette1, 0, -10)


def bas1(event):
    global R1Y, Hauteur
    """mouvement vers le bas de la raquette 1"""
    R1Y = R1Y + 10
    if (R1Y+RHauteur/2) > Hauteur :
        R1Y = R1Y - 10
    else :
        MonCanevas.move(Raquette1, 0, 10)


def haut2(event):
    global R2Y
    """mouvement vers le haut de la raquette 2"""
    R2Y = R2Y - 10
    if (R2Y-RHauteur/2) < 0 :
        R2Y = R2Y + 10
    else :
        MonCanevas.move(Raquette2, 0, -10)

def bas2 (event):
    global R2Y, Hauteur
    """mouvement vers le bas de la raquette 2"""
    R2Y = R2Y + 10
    if (R2Y+RHauteur/2) > Hauteur :
        R2Y = R2Y - 10
    else :
        MonCanevas.move(Raquette2, 0, 10)

#PROGRAMME PRINCIPAL
Mafenetre.title('Dan Du')
photo = PhotoImage(file="jeuPing/fond.gif")
# création d'un widget 'Canvas'
MonCanevas = Canvas(Mafenetre,
 width = Largeur, height = Hauteur)
MonCanevas.pack(side = TOP, padx = 10, pady = 10)
item = MonCanevas.create_image(0, 0,
 anchor=NW, image=photo)
# Création d'un objet graphique balle
Balle = MonCanevas.create_oval(X-Rayon, Y-Rayon,
 X+Rayon, Y+Rayon, width=1, fill='white')
Bouton1 = Button(Mafenetre, text = 'Quitter',
 command = Mafenetre.destroy)
Bouton1.pack()
# Création d'un objet graphique raquette
R1X = 1010
R1Y = Hauteur/2
R2X = 10
R2Y = Hauteur/2
Raquette1 = MonCanevas.create_rectangle(R1X, R1Y-RHauteur/2,
 R1X+RLargeur, R1Y+RHauteur/2, outline='white', fill='white')
Raquette2 = MonCanevas.create_rectangle(R2X, R2Y-RHauteur/2,
 R2X+RLargeur, R2Y+RHauteur/2, outline='white', fill='white')
#Association des movements aux touches du clavier
MonCanevas.bind_all("z", haut2)
MonCanevas.bind_all("s", bas2)
MonCanevas.bind_all("<Up>", haut1)
MonCanevas.bind_all("<Down>", bas1)
lbScore1.pack(side=LEFT, padx=5, pady=0)
lbScore2.pack(side=RIGHT, padx=5, pady=0)
deplacement_balle()
Mafenetre.mainloop()
pygame.mixer.stop()
