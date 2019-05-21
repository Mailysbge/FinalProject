from tkinter import *


class Morpion:

    def clic(self, event):
        """ Gestion de l'événement clic gauche sur la zone graphique """
        # position du pointeur de la souris
        x = event.x
        y = event.y
        if 1 <= x <= 183:
            colonne = 1
        elif 184 <= x <= 366:
            colonne = 2
        elif 367 <= x <= 550:
            colonne = 3
        if 1 <= y <= 183:
            ligne = 1
        elif 184 <= y <= 366:
            ligne = 2
        elif 367 <= y <= 550:
            ligne = 3
        nombre_case = ligne*3 + (colonne - 3)
        if nombre_case == 1 and not 1 in self.joueur1 and not 1 in self.joueur2\
        and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                12, 12, anchor = NW, image = self.croix)
            self.joueur1.append(1)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 2 and not 2 in self.joueur1 and not 2 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                196, 12, anchor = NW, image = self.croix)
            self.joueur1.append(2)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 3 and not 3 in self.joueur1 and not 3 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                380, 12, anchor = NW, image = self.croix)
            self.joueur1.append(3)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 4 and not 4 in self.joueur1 and not 4 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                12, 196, anchor = NW, image = self.croix)
            self.joueur1.append(4)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 5 and not 5 in self.joueur1 and not 5 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                196, 196, anchor = NW, image = self.croix)
            self.joueur1.append(5)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 6 and not 6 in self.joueur1 and not 6 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                380, 196, anchor = NW, image = self.croix)
            self.joueur1.append(6)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 7 and not 7 in self.joueur1 and not 7 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                12, 380, anchor = NW, image = self.croix)
            self.joueur1.append(7)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 8 and not 8 in self.joueur1 and not 8 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                196, 380, anchor = NW, image = self.croix)
            self.joueur1.append(8)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 9 and not 9 in self.joueur1 and not 9 in\
         self.joueur2 and\
                self.joueur % 2 == 0:
            self.item = self.Canevas.create_image(
                380, 380, anchor = NW, image = self.croix)
            self.joueur1.append(9)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur1):
                self.fenetre1()
        elif nombre_case == 1 and not 1 in self.joueur2 and not 1 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                12, 12, anchor = NW, image = self.cercle)
            self.joueur2.append(1)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 2 and not 2 in self.joueur2 and not 2 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                196, 12, anchor = NW, image = self.cercle)
            self.joueur2.append(2)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 3 and not 3 in self.joueur2 and not 3 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                380, 12, anchor = NW, image = self.cercle)
            self.joueur2.append(3)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 4 and not 4 in self.joueur2 and not 4 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                12, 196, anchor = NW, image = self.cercle)
            self.joueur2.append(4)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 5 and not 5 in self.joueur2 and not 5 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                196, 196, anchor = NW, image = self.cercle)
            self.joueur2.append(5)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 6 and not 6 in self.joueur2 and not 6 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                380, 196, anchor = NW, image = self.cercle)
            self.joueur2.append(6)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 7 and not 7 in self.joueur2 and not 7 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                12, 380, anchor = NW, image = self.cercle)
            self.joueur2.append(7)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 8 and not 8 in self.joueur2 and not 8 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                196, 380, anchor = NW, image = self.cercle)
            self.joueur2.append(8)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()
        elif nombre_case == 9 and not 9 in self.joueur2 and not 9 in\
         self.joueur1 and\
                self.joueur % 2 == 1:
            self.item = self.Canevas.create_image(
                380, 380, anchor = NW, image = self.cercle)
            self.joueur2.append(9)
            self.joueur = self.joueur + 1
            if self.gagne(self.joueur2):
                self.fenetre2()

    def gagne(self, l):
        """vérifie si un joueur a une combinaison gagnante"""
        return (1 in l and 2 in l and 3 in l) or (1 in l and 5 in l and 9 in l)\
         or (1 in l and 4 in l and 7 in l) or (4 in l and 5 in l and 6 in l) or\
            (7 in l and 8 in l and 9 in l) or (7 in l and 5 in l and 3 in l) or\
            (2 in l and 5 in l and 8 in l) or (6 in l and 9 in l and 3 in l)

    def fenetre2(self):
        """création de la fenêtre de fin"""
    # Création de la fenêtre principale (main window)
        fenetre2 = Tk()
    # Création d'un widget Label (texte 'le joueur 1 a gagné')
        label1 = Label(fenetre2, text = 'le joueur rond a gagné', fg = 'red')
    # Positionnement du widget avec la méthode pack()
        label1.pack()
    # Création d'un widget Button (bouton Quitter)
        bouton1 = Button(fenetre2, text = 'Quitter', command = fenetre2.destroy)
        bouton1.pack()
    # Lancement du gestionnaire d'événements
        fenetre2.mainloop()

    def fenetre1(self):
        """création de la fenêtre de fin"""
    # Création de la fenêtre principale (main window)
        fenetre1 = Tk()
    # Création d'un widget Label (texte 'le joueur 2 a gagné')
        label1 = Label(fenetre1, text = 'le joueur croix a gagné', fg = 'red')
    # Positionnement du widget avec la méthode pack()
        label1.pack()
    # Création d'un widget Button (bouton Quitter)
        bouton1 = Button(fenetre1, text ='OK', command = fenetre1.destroy)
        bouton1.pack()
    # Lancement du gestionnaire d'événements
        fenetre1.mainloop()

    def createFrame(self, window, callbackExit):
        """Ce qui permet de relier le morpion a l'interface d'accueil"""
        self.joueur = 0

        self.joueur1 = []
        self.joueur2 = []

        # Création de la fenêtre principale (main window)
        frame = Frame(window)
        frame.pack()
        # image du cercle
        self.cercle = PhotoImage(file = "morpion/cercle.png")
        # image de la croix
        self.croix = PhotoImage(file = "morpion/croix.png")
        # Image de fond
        self.photo = PhotoImage(file = "morpion/quadrillage.png")
        # Création d'un widget Canvas (zone graphique)
        largeur = 550
        hauteur = 550
        self.Canevas = Canvas(frame, width = largeur, height = hauteur)
        self.item = self.Canevas.create_image(
        2, 2, anchor = NW, image = self.photo)
        self.Canevas.pack()

        bouton1 = Button(frame, text = 'Quitter', command = callbackExit)
        bouton1.pack()
        self.Canevas.bind('<Button - 1>', self.clic)
        self.Canevas.pack(padx = 5, pady = 5)

        return frame
