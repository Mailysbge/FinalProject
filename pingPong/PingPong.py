from tkinter import *
import pygame
import random
import math
from PIL import Image, ImageTk


class PingPong:
    def deplacement_balle(self):
        """ Déplacement de la balle """
        # rebond à droite
        if self.X+self.Rayon+self.DX > self.Largeur:
            self.score_1 += 1
            self.lbScore1['text'] = "Joueur 1 : " + format(str(self.score_1))
            self.X = self.Largeur / 2
            self.Y = self.Hauteur / 2
            self.DX = self.vitesse*math.cos(self.angle)
            self.DY = self.vitesse*math.sin(self.angle)

        # rebond à gauche
        if self.X-self.Rayon+self.DX < 0:
            self.score_2 += 1
            self.lbScore2['text'] = "Joueur 2 : " + format(str(self.score_2))
            self.X = self.Largeur / 2
            self.Y = self.Hauteur / 2
            self.DX = self.vitesse*math.cos(self.angle)
            self.DY = self.vitesse*math.sin(self.angle)

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
        if (self.Y+self.DY > self.R2Y - self.RHauteur/2) and (self.Y+self.DY < self.R2Y + self.RHauteur/2):
            if (self.X+self.DX < self.R2X+self.RLargeur):
                self.DX = -self.DX

        self.X = self.X+self.DX
        self.Y = self.Y+self.DY

        # affichage
        self.MonCanevas.coords(self.Balle, self.X-self.Rayon,
                               self.Y-self.Rayon, self.X+self.Rayon, self.Y+self.Rayon)

        # mise à jour toutes les 50 ms
        self.frame.after(50, self.deplacement_balle)

    def haut1(self, event):
        """mouvement vers le haut de la raquette 1"""
        self.R1Y = self.R1Y - 10
        if (self.R1Y-self.RHauteur/2) < 0:
            self.R1Y = self.R1Y + 10
        else:
            self.MonCanevas.move(self.Raquette1, 0, -10)

    def bas1(self, event):
        """mouvement vers le bas de la raquette 1"""
        self.R1Y = self.R1Y + 10
        if (self.R1Y+self.RHauteur/2) > self.Hauteur:
            self.R1Y = self.R1Y - 10
        else:
            self.MonCanevas.move(self.Raquette1, 0, 10)

    def haut2(self, event):
        """mouvement vers le haut de la raquette 2"""
        self.R2Y = self.R2Y - 10
        if (self.R2Y-self.RHauteur/2) < 0:
            self.R2Y = self.R2Y + 10
        else:
            self.MonCanevas.move(self.Raquette2, 0, -10)

    def bas2(self, event):
        """mouvement vers le bas de la raquette 2"""
        self.R2Y = self.R2Y + 10
        if (self.R2Y+self.RHauteur/2) > self.Hauteur:
            self.R2Y = self.R2Y - 10
        else:
            self.MonCanevas.move(self.Raquette2, 0, 10)

    def createFrame(self, window, callbackExit):
        self.frame = Frame(window)
        self.frame.pack()

        self.Largeur = 1024  # en pixels
        self.Hauteur = 700

        self.lbScore1 = Label(self.frame, text="")
        self.lbScore2 = Label(self.frame, text="")
        self.score_1 = 0
        self.score_2 = 0

        self.R1X = 0
        self.R1Y = 0
        self.R2X = 0
        self.R2Y = 0

        self.RHauteur = 160
        self.RLargeur = 5

        # Musique du jeu
        pygame.mixer.init()
        pygame.mixer.Sound("pingPong/ping-pong-song.wav").play(-1)
        self.Rayon = 7  # rayon de la balle

        # position initiale au milieu
        self.X = self.Largeur/2
        self.Y = self.Hauteur/2

        # direction initiale aléatoire
        self.vitesse = random.uniform(1.8, 2)*5
        self.angle = random.uniform(0, 2*math.pi)
        self.DX = self.vitesse*math.cos(self.angle)
        self.DY = self.vitesse*math.sin(self.angle)

        self.photo = PhotoImage(file="pingPong/fond.gif")
        # création d'un widget 'Canvas'
        self.MonCanevas = Canvas(self.frame,
                                 width=self.Largeur, height=self.Hauteur)
        self.MonCanevas.pack(side=TOP, padx=10, pady=10)
        self.item = self.MonCanevas.create_image(0, 0,
                                                 anchor=NW, image=self.photo)
        # Création d'un objet graphique balle
        self.Balle = self.MonCanevas.create_oval(self.X-self.Rayon, self.Y-self.Rayon,
                                                 self.X+self.Rayon, self.Y+self.Rayon, width=1, fill='white')
        self.Bouton1 = Button(self.frame, text='Quitter',
                              command=callbackExit)
        self.Bouton1.pack()
        # Création d'un objet graphique raquette
        self.R1X = 1010
        self.R1Y = self.Hauteur/2
        self.R2X = 10
        self.R2Y = self.Hauteur/2
        self.Raquette1 = self.MonCanevas.create_rectangle(self.R1X, self.R1Y-self.RHauteur/2,
                                                          self.R1X+self.RLargeur, self.R1Y+self.RHauteur/2, outline='white', fill='white')
        self.Raquette2 = self.MonCanevas.create_rectangle(self.R2X, self.R2Y-self.RHauteur/2,
                                                          self.R2X+self.RLargeur, self.R2Y+self.RHauteur/2, outline='white', fill='white')
        # Association des movements aux touches du clavier
        self.MonCanevas.bind_all("z", self.haut2)
        self.MonCanevas.bind_all("s", self.bas2)
        self.MonCanevas.bind_all("<Up>", self.haut1)
        self.MonCanevas.bind_all("<Down>", self.bas1)
        self.lbScore1.pack(side=LEFT, padx=5, pady=0)
        self.lbScore2.pack(side=RIGHT, padx=5, pady=0)
        self.deplacement_balle()

        return self.frame
