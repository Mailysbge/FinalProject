from tkinter import *
import pygame
import random
import math
from PIL import Image, ImageTk


class PingPong:

    def deplacement_balle(self):
        """ Déplacement de la balle """
        # rebond à droite
        if self.x + self.rayon + self.dX > self.largeur:
            self.score_1  += 1
            self.lbScore1['text'] = "Joueur 1 : " + format(str(self.score_1))
            self.x = self.largeur / 2
            self.y = self.hauteur / 2
            self.dX = self.vitesse * math.cos(self.angle)
            self.dY = self.vitesse * math.sin(self.angle)


        # rebond à gauche
        if self.x - self.rayon + self.dX < 0:
            self.score_2 += 1
            self.lbScore2['text'] = "Joueur 2 : " + format(str(self.score_2))
            self.x = self.largeur / 2
            self.y = self.hauteur / 2
            self.dX = self.vitesse * math.cos(self.angle)
            self.dY = self.vitesse * math.sin(self.angle)


        # rebond en bas
        if self.y + self.rayon + self.dY > self.hauteur:
            self.y = 2 * (self.hauteur - self.rayon) - self.y
            self.dY =  - self.dY


        # rebond en haut
        if self.y - self.rayon + self.dY < 0:
            self.y = 2 * self.rayon - self.y
            self.dY =  - self.dY


        # Rebond raquette 1
        if (self.y + self.dY > self.r1Y - self.rHauteur/2) and (self.y +
         self.dY <
        self.r1Y + self.rHauteur/2):
            if (self.x + self.dX > self.r1X):
                self.dX =  - self.dX


        # Rebond raquette 2
        if (self.y + self.dY > self.r2Y - self.rHauteur/2) and (self.y +
         self.dY <
        self.r2Y + self.rHauteur/2):
            if (self.x + self.dX < self.r2X + self.rLargeur):
                self.dX =  - self.dX


        self.x = self.x + self.dX
        self.y = self.y + self.dY

        # affichage
        self.monCanevas.coords(self.balle, self.x - self.rayon,
                               self.y - self.rayon, self.x + self.rayon,
                                self.y +
                               self.rayon)

        # mise à jour toutes les 50 ms
        self.frame.after(50, self.deplacement_balle)

    def haut1(self, event):
        """mouvement vers le haut de la raquette 1"""
        self.r1Y = self.r1Y - 10
        if (self.r1Y - self.rHauteur/2) < 0:
            self.r1Y = self.r1Y + 10
        else:
            self.monCanevas.move(self.raquette1, 0,  - 10)

    def bas1(self, event):
        """mouvement vers le bas de la raquette 1"""
        self.r1Y = self.r1Y + 10
        if (self.r1Y + self.rHauteur/2) > self.hauteur:
            self.r1Y = self.r1Y - 10
        else:
            self.monCanevas.move(self.raquette1, 0, 10)

    def haut2(self, event):
        """mouvement vers le haut de la raquette 2"""
        self.r2Y = self.r2Y - 10
        if (self.r2Y - self.rHauteur/2) < 0:
            self.r2Y = self.r2Y + 10
        else:
            self.monCanevas.move(self.raquette2, 0,  - 10)

    def bas2(self, event):
        """mouvement vers le bas de la raquette 2"""
        self.r2Y = self.r2Y + 10
        if (self.r2Y + self.rHauteur/2) > self.hauteur:
            self.r2Y = self.r2Y - 10
        else:
            self.monCanevas.move(self.raquette2, 0, 10)

    def createFrame(self, window, callbackExit):
        self.frame = Frame(window)
        self.frame.pack()

        self.largeur = 1024  # en pixels
        self.hauteur = 700

        self.lbScore1 = Label(self.frame, text = "")
        self.lbScore2 = Label(self.frame, text = "")
        self.score_1 = 0
        self.score_2 = 0

        self.r1X = 0
        self.r1Y = 0
        self.r2X = 0
        self.r2Y = 0

        self.rHauteur = 160
        self.rLargeur = 5

        # Musique du jeu
        pygame.mixer.init()
        pygame.mixer.Sound("pingPong/ping-pong-song.wav").play( - 1)
        self.rayon = 7  # rayon de la balle

        # position initiale au milieu
        self.x = self.largeur/2
        self.y = self.hauteur/2

        # direction initiale aléatoire
        self.vitesse = random.uniform(1.8, 2) * 5
        self.angle = random.uniform(0, 2 * math.pi)
        self.dX = self.vitesse * math.cos(self.angle)
        self.dY = self.vitesse * math.sin(self.angle)

        self.photo = PhotoImage(file = "pingPong/fond.gif")
        # création d'un widget 'Canvas'
        self.monCanevas = Canvas(self.frame,
        width = self.largeur, height = self.hauteur)
        self.monCanevas.pack(side = TOP, padx = 10, pady = 10)
        self.item = self.monCanevas.create_image(0, 0,
        anchor = NW, image = self.photo)
        # Création d'un objet graphique balle
        self.balle = self.monCanevas.create_oval(self.x - self.rayon, self.y -
        self.rayon, self.x + self.rayon, self.y +  self.rayon,
        width = 1, fill = 'white')
        self.bouton1 = Button(self.frame, text = 'Quitter',
         command = callbackExit)
        self.bouton1.pack()
        # Création d'un objet graphique raquette
        self.r1X = 1010
        self.r1Y = self.hauteur/2
        self.r2X = 10
        self.r2Y = self.hauteur/2
        self.raquette1 = self.monCanevas.create_rectangle(self.r1X,
         self.r1Y - self.rHauteur/2,
        self.r1X + self.rLargeur, self.r1Y + self.rHauteur/2,
         outline = 'white', fill = 'white')
        self.raquette2 = self.monCanevas.create_rectangle(self.r2X,
         self.r2Y - self.rHauteur/2,
         self.r2X + self.rLargeur, self.r2Y + self.rHauteur/2,
          outline = 'white',
          fill = 'white')
        # Association des movements aux touches du clavier
        self.monCanevas.bind_all("z", self.haut2)
        self.monCanevas.bind_all("s", self.bas2)
        self.monCanevas.bind_all("<Up>", self.haut1)
        self.monCanevas.bind_all("<Down>", self.bas1)
        self.lbScore1.pack(side = LEFT, padx = 5, pady = 0)
        self.lbScore2.pack(side = RIGHT, padx = 5, pady = 0)
        self.deplacement_balle()


        return self.frame





































