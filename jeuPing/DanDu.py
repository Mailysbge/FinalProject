from tkinter import *
import pygame
import random
import math
from PIL import Image, ImageTk

class DanDu:

    def __init__(self, ):

        self.Largeur = 1024 # en pixels
        self.Hauteur = 700

        self.lbScore1 = Label(Mafenetre, text="")
        self.lbScore2 = Label(Mafenetre, text="")
        self.score_1 = 0
        self.score_2 = 0

        self.R1X = 0
        self.R1Y = 0
        self.R2X = 0
        self.R2Y = 0

        self.RHauteur = 160
        self.RLargeur = 5

        self.callbackExit = None
        self.frame = None

        self.Rayon = 7 # rayon de la balle

        # position initiale au milieu
        self.X = Largeur/2
        self.Y = Hauteur/2

        # direction initiale aléatoire
        self.vitesse = random.uniform(1.8, 2)*5
        self.angle = random.uniform(0, 2*math.pi)
        self.DX = vitesse*math.cos(angle)
        self.DY = vitesse*math.sin(angle)


    def deplacement_balle():

        """ Déplacement de la balle """
        global X,Y,DX,DY,Rayon,Largeur,Hauteur,RX1,RY1,RX2,RY2,RHauteur,RLargeur,score_1,score_2,lbScore1

        # rebond à droite
        if self.X+self.Rayon+self.DX > self.Largeur:
            self.score_1 += 1
            self.lbScore1['text'] = "Joueur 1 : " + format(str(score_1))
            self.X = Largeur / 2
            self.Y = Hauteur / 2
            self.DX = vitesse*math.cos(angle)
            self.DY = vitesse*math.sin(angle)

        # rebond à gauche
        if self.X-self.Rayon+self.DX < 0:
            self.score_2 += 1
            self.lbScore2['text'] = "Joueur 2 : " + format(str(score_2))
            self.X = Largeur / 2
            self.Y = Hauteur / 2
            self.DX = vitesse*math.cos(angle)
            self.DY = vitesse*math.sin(angle)

        # rebond en bas
        if self.Y+self.Rayon+self.DY > self.Hauteur:
            self.Y = 2*(self.Hauteur-self.Rayon)-self.Y
            self.DY = -self.DY

        # rebond en haut
        if self.Y-self.Rayon+self.DY < 0:
            self.Y = 2*self.Rayon-self.Y
            self.DY = -self.DY

        # Rebond raquette 1
        if (self.Y+self.DY > self.R1Y - self.RHauteur/2) and (self.Y+self.DY < self.R1Y + self.RHauteur/2):
            if (self.X+self.DX > self.R1X):
                self.DX = -self.DX

        # Rebond raquette 2
        if (self.Y+self.DY > self.R2Y - self.RHauteur/2) and (self.Y+DY < self.R2Y + self.RHauteur/2):
            if (self.X+DX < self.R2X+self.RLargeur):
                self.DX = -self.DX

        self.X = self.X+self.DX
        self.Y = self.Y+self.DY

        # affichage
        MonCanevas.coords(Balle, self.X-self.Rayon,
        self.Y-self.Rayon, self.X+self.Rayon, self.Y+self.Rayon)

        # mise à jour toutes les 50 ms
        Mafenetre.after(50, deplacement_balle)

    def haut1(event):
        self.R1Y
        """mouvement vers le haut de la raquette 1"""
        self.R1Y = self.R1Y - 10
        if (self.R1Y-self.RHauteur/2) < 0 :
            self.R1Y = self.R1Y + 10
        else :
            MonCanevas.move(Raquette1, 0, -10)


    def bas1(event):
        global R1Y, Hauteur
        """mouvement vers le bas de la raquette 1"""
        self.R1Y = self.R1Y + 10
        if (self.R1Y+self.RHauteur/2) > self.Hauteur :
            self.R1Y = self.R1Y - 10
        else :
            MonCanevas.move(Raquette1, 0, 10)


    def haut2 (event):
        self.R2Y
        """mouvement vers le haut de la raquette 2"""
        self.R2Y = self.R2Y - 10
        if (self.R2Y-self.RHauteur/2) < 0 :
            self.R2Y = self.R2Y + 10
        else :
            MonCanevas.move(Raquette2, 0, -10)

    def bas2 (event):
        self.R2Y, self.Hauteur
        """mouvement vers le bas de la raquette 2"""
        self.R2Y = self.R2Y + 10
        if (self.R2Y+self.RHauteur/2) > self.Hauteur :
            self.R2Y = self.R2Y - 10
        else :
            MonCanevas.move(Raquette2, 0, 10)

    def musique():
        #Musique du jeu
        pygame.mixer.init()
        pygame.mixer.Sound('jeuPing/ping-pong-song.wav').play(-1)

    def imageDeFond():
        photo = PhotoImage(file="jeuPing/fond.gif")

    def creationCanvas():
        # création d'un widget 'Canvas'
        Mafenetre = Tk()
        MonCanevas = Canvas(Mafenetre,
        width = self.Largeur, height = self.Hauteur)
        MonCanevas.pack(side = TOP, padx = 10, pady = 10)
        item = MonCanevas.create_image(0, 0,
        anchor=NW, image=photo)

    def balle():
        # Création d'un objet graphique balle
        Balle = MonCanevas.create_oval(self.X-self.Rayon, self.Y-self.Rayon,
        self.X+self.Rayon, self.Y+self.Rayon, width=1, fill='white')
        Bouton1 = Button(Mafenetre, text = 'Quitter',
        command = Mafenetre.destroy)
        Bouton1.pack()

    def raquette():
        # Création d'un objet graphique raquette
        self.R1X = 1010
        self.R1Y = self.Hauteur/2
        self.R2X = 10
        self.R2Y = self.Hauteur/2
        Raquette1 = MonCanevas.create_rectangle(self.R1X, self.R1Y-self.RHauteur/2,
        self.R1X+self.RLargeur, self.R1Y+self.RHauteur/2, outline='white', fill='white')
        Raquette2 = MonCanevas.create_rectangle(self.R2X, self.R2Y-self.RHauteur/2,
        self.R2X+self.RLargeur, self.R2Y+self.RHauteur/2, outline='white', fill='white')

    def mouvementClavier():
        #Association des movements aux touches du clavier
        MonCanevas.bind_all("z", haut2)
        MonCanevas.bind_all("s", bas2)
        MonCanevas.bind_all("<Up>", haut1)
        MonCanevas.bind_all("<Down>", bas1)
        lbScore1.pack(side=LEFT, padx=5, pady=0)
        lbScore2.pack(side=RIGHT, padx=5, pady=0)
        deplacement_balle()
        pygame.mixer.stop()

    def createFrame(self, window, callbackExit):
        self.callbackExit = callbackExit
        self.frame = Frame(window)
        self.frame.pack()
        return self.frame

    def menus_PingPong(self, fen):
        top = Menu(fen)
        fen.config(menu = top)

        jeu = Menu(top, tearoff = False)
        top.add_cascade(label = 'Options', menu=jeu)
        jeu.add_command(label = 'Nouvelle partie', command = )

        jeu.add_command(label = 'Quitter', command=self.callbackExit)