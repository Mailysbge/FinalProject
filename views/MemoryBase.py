from tkinter import *
from random import randint, shuffle


class MemoryBase:
    def __init__(self, ):
        # ----- variables globales ---------------------------------------------------
        self.images = []         # contient les liens aux fichiers images
        self.cartes = []         # contient le lien vers l'image des différentes cartes
        self.cartes_jouees = []  # contient les cartes jouées
        self.nb_lignes = 5
        self.nb_colonnes = 4
        self.joueur_actuel = 0
        self.score = [0, 0]
        self.fini = False
        self.peut_jouer = True
        self.canvas = None
        self.frame = None
        self.points_joueur1 = None
        self.points_joueur2 = None
        self.callbackExit = None

    # ----- Images ----------------------------------------------------------------

    def charger_images(self):
        del self.images[:]   # vide la liste
        nb_images = 21  # l'image numéro 0 est le dos des cartes
        choixCartes = []
        choixCartes.append(0)
        i = 0
        while i < nb_images-1:           # tirage au sort des cartes à utiliser
            x = randint(1, nb_images-1)
            if x not in choixCartes:
                choixCartes.append(x)
                i += 1
        for i in range(nb_images):           # importation des images
            nom = 'cartes/carte-' + str(choixCartes[i]) + '.gif'
            image = PhotoImage(file=nom)
            self.images.append(image)

    # ----- Melange des cartes -----------------------------------------------------

    def melanger_cartes(self):
        nb_cartes = self.nb_colonnes * self.nb_lignes
        self.cartes = list(range(1, nb_cartes//2+1))*2
        shuffle(self.cartes)

    # ----- Retourne les deux cartes à la fin de la sélection ----------------------

    def gerer_tirage(self):
        if self.cartes[self.cartes_jouees[0]-1] == self.cartes[self.cartes_jouees[1]-1]:
            # enlève les cartes identiques. Le joueur actuel reste le même
            self.canvas.delete(self.cartes_jouees[0])
            self.canvas.delete(self.cartes_jouees[1])
            self.score[self.joueur_actuel] += 1
        else:
            # retourne les cartes différentes. Le joueur actuel change
            self.canvas.itemconfig(self.cartes_jouees[0], image=self.images[0])
            self.canvas.itemconfig(self.cartes_jouees[1], image=self.images[0])
            # la main passe à l'autre joueur
            self.joueur_actuel = (self.joueur_actuel+1) % 2
        self.cartes_jouees = []
        text1 = 'Joueur 1 : ' + str(self.score[0]*2)
        text2 = 'Joueur 2 : ' + str(self.score[1]*2)
        self.points_joueur1.config(text=text1)
        self.points_joueur2.config(text=text2)
        self.peut_jouer = True           # réactive l'effet du clic de la souris
        if self.joueur_actuel == 0:      # celui qui joue est en orange
            self.points_joueur1.config(bg='orange')
            self.points_joueur2.config(bg='white')
        else:
            self.points_joueur2.config(bg='orange')
            self.points_joueur1.config(bg='white')
        if self.score[0] + self.score[1] == (self.nb_colonnes*self.nb_lignes)//2:
            self.fini = True               # afficher le résultat de la partie
            if self.score[0] > self.score[1]:
                texte = "Le joueur 1 a gagné !"
            elif self.score[0] < self.score[1]:
                texte = "Le joueur 2 a gagné !"
            else:
                texte = "Egalité !"
            self.canvas.create_rectangle(0, 0, (110*self.nb_colonnes)+20, (110*self.nb_lignes)+20,
                                         fill='white')
            self.canvas.create_text((55*self.nb_colonnes)+10, (55*self.nb_lignes)+10,
                                    text=texte, font='Calibri 24', fill='black')

    # ----- Retourne la carte sélectionnée -----------------------------------------
    def cliquer_carte(self, event):
        if len(self.cartes_jouees) < 2:
            carteSel = self.canvas.find_closest(event.x, event.y)
            carteID = carteSel[0]
            if self.fini:
                self.fini = False
                self.reinit()
            else:
                self.canvas.itemconfig(
                    carteID, image=self.images[self.cartes[carteID-1]])  # montre la carte
                if len(self.cartes_jouees) == 0:
                    # enregistre la carte jouée
                    self.cartes_jouees.append(carteID)
                # ne pas cliquer 2x sur la même carte !
                elif carteID != self.cartes_jouees[0]:
                    self.cartes_jouees.append(carteID)
        if self.peut_jouer and len(self.cartes_jouees) == 2:
            self.peut_jouer = False                  # désactive l'effet du clic de la souris
            # patiente 1,5 secondes avant de continuer
            self.frame.after(1500, self.gerer_tirage)

    # ----- création des menus et sous-menus ------------------------------------------
    def creer_menus(self, fen):
        top = Menu(fen)
        fen.config(menu=top)

        jeu = Menu(top, tearoff=False)
        top.add_cascade(label='Options', menu=jeu)
        jeu.add_command(label='Nouvelle partie', command=self.reinit)

        jeu.add_command(label='Quitter', command=self.callbackExit)

    # ----- Création du canvas --------------------------------------------------------
    def creer_canevas(self, fen, col, lig):
        return Canvas(fen, width=(110*col)+10, height=(110*lig)+10, bg='white')

    # ----- Modifier le canvas --------------------------------------------------------
    # Redémarre une partie et change éventuellement la difficulté

    def reinit(self):
        self.joueur_actuel = 0
        self.score = [0, 0]
        del self.cartes[:]
        del self.cartes_jouees[:]
        if (self.canvas is not None):
            self.canvas.destroy()
        if (self.points_joueur1 is not None):
            self.points_joueur1.destroy()
        if (self.points_joueur2 is not None):
            self.points_joueur2.destroy()
        # création du canvas dont la taille dépend du nombre de cartes
        self.canvas = self.creer_canevas(
            self.frame, self.nb_colonnes, self.nb_lignes)
        self.canvas.pack(side=TOP, padx=2, pady=2)
        self.points_joueur1 = Label(self.frame, text="Joueur 1 : 0",
                                    bg="blue", font="Helvetica 16")
        self.points_joueur1.pack(pady=2, side=LEFT)
        self.points_joueur2 = Label(
            self.frame, text="Joueur 2 : 0", bg="white", font="Helvetica 16")
        self.points_joueur2.pack(pady=2, side=RIGHT)
        self.charger_images()
        self.melanger_cartes()
        for i in range(self.nb_colonnes):                # dessin des cartes retournées
            for j in range(self.nb_lignes):
                self.canvas.create_image(
                    (110*i)+60, (110*j)+60, image=self.images[0])
        # permet le clic sur les cartes
        self.canvas.bind("<Button-1>", self.cliquer_carte)

    # ----- Programme principal ----------------------------------------------------
    def createFrame(self, window, callbackExit):
        self.callbackExit = callbackExit
        self.frame = Frame(window)
        self.frame.pack()
        self.creer_menus(window)

        self.reinit()

        return self.frame
