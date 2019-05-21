from tkinter import *
from random import randint, shuffle

class MemoryBase:
    """Classe de mon mini-jeu Memory pour le jeu en multijoueurs Arena Games """

    def __init__(self, ):
        """Méthode de classe"""

        #Listes de l'instance.--------------------------------------------------
        #contient les liens aux fichiers images.
        self.images = []
        #contient le lien vers l'image (impact) des différentes cartes.
        #image != cartes
        self.cartes = []
        #contient les cartes choisie, ce sera toujours deux nombres entier, ces
        #dernier indique l'emplacement des cartes.
        self.cartes_jouees = []
        #le score des joueurs.
        self.score = [0, 0]

        #Variables d'instances avec leur paramètres nommés.---------------------
        #définie le nombre de ligne.
        self.nb_lignes = 5
        #définie le nombre de colonnes.
        self.nb_colonnes = 4
        #la variable pour le joueur qui joue.
        self.joueur_actuel = 0
        #définie le moment ou la partie est finie.

        #variables booléennes---------------------------------------------------
        self.fini = False
        #définie c'est à qui de jouer
        self.peut_jouer = True
        #zone rectangulaire destinée à contenir les cartes.
        self.canvas = None
        #Un frame est un conteneur pour d’autre widgets.
        self.frame = None
        #score du joueur 1.
        self.points_joueur1 = None
        #score du joueur 2.
        self.points_joueur2 = None
        #Un callback, c'est une fonction passée en paramètre quiva être appelée\
        #à une condition. La condition est “quand\
        #ceci arrive”et “ceci” est “quand le traitement est terminé”."""
        self.callbackExit = None

    def images_chargement(self):
        """ Fonction qui gérerera le chargement des cartes"""
        #ça supprime/vide tout le contenu de la liste
        del self.images[:]
        # j'assigne une valeur à ma variable qui correspond au nombre de cartes
        nb_images = 21
        choixCartes = []
        #La méthode append() ajoute les éléments dans une liste mais conserve la
        #forme d'itérable. L'itérable sera ajouté/ importé comme un nouvel
        #élément de la liste.
        choixCartes.append(0)
        i = 0
        while i < nb_images - 1:
            #randint est une fontion intégré du module random, elle peut générer
            #des nombres aléatoires.
            x = randint(1, nb_images - 1)
            if x not in choixCartes:
                # tirage au sort des cartes à utiliser
                choixCartes.append(x)
                i += 1
        for i in range(nb_images):
            #on va chercher la carte dans le dossier
            nom = 'memory/cartes/carte-' + str(choixCartes[i]) + '.gif'
            # importation des images
            image = PhotoImage(file = nom)
            self.images.append(image)

    def cartes_melanges(self):
        """ Fonction qui permet le mélange des cartes"""
        #les images sont placé deux fois dans liste images
        #Shuffle permet le mélange aléatoire des cartes.
        nb_cartes = self.nb_colonnes * self.nb_lignes
        self.cartes = list(range(1, nb_cartes//2 + 1)) * 2
        shuffle(self.cartes)

    def tirage(self):
        """ Fonction qui gère le "tirage" des cartes"""
        #si l'emplacement de la carte est identique (=carte identique)...
        if self.cartes[self.cartes_jouees[0] - 1] == self.cartes\
        [self.cartes_jouees[1] - 1]:
            # ... enlève les cartes identiques. Le joueur actuel reste le même
            self.canvas.delete(self.cartes_jouees[0])
            self.canvas.delete(self.cartes_jouees[1])
            self.score[self.joueur_actuel] += 1

        else:
            # sinon retourne les cartes différentes. Le joueur actuel change.
            self.canvas.itemconfig(self.cartes_jouees[0],
             image = self.images[0])
            self.canvas.itemconfig(self.cartes_jouees[1],
             image = self.images[0])
            # la main passe à l'autre joueur.
            self.joueur_actuel = (self.joueur_actuel + 1) % 2

        self.cartes_jouees = []
        text1 = 'Player 1 : ' + str(self.score[0] * 2)
        text2 = 'Player 2 : ' + str(self.score[1] * 2)
        self.points_joueur1.config(text = text1)
        self.points_joueur2.config(text = text2)
        # réactive l'effet du clic de la souris
        self.peut_jouer = True

        if self.joueur_actuel == 0:
             # celui qui joue, le joueur 1 est en lightcoral
            self.points_joueur1.config(bg ='lightcoral')
            # celui qui ne joue pas le joueur 2 est en blanc
            self.points_joueur2.config(bg ='white')

        else:
            # celui qui joue, le joueur 2 est en lightcoral
            self.points_joueur2.config(bg = 'lightcoral')
            # celui qui ne joue pas le joueur 1 est en blanc
            self.points_joueur1.config(bg = 'white')

        if self.score[0] + self.score[1] == \
        (self.nb_colonnes * self.nb_lignes)//2:
            #si le jeu est fini
            self.fini = True
            #il n'y plus de cartes on s'occupe du gagnant de la partie
            if self.score[0] > self.score[1]:
                texte = "Player 1 has won !"
            elif self.score[0] < self.score[1]:
                texte = "Player 2 has won !"
            else:
                texte = "Equality !"
             #décor de l'affichage des résultats
            self.canvas.create_rectangle(0, 0, (110 * self.nb_colonnes) + 20,
             (110 * self.nb_lignes) + 20,
                                         fill = 'salmon')
            self.canvas.create_text((55 * self.nb_colonnes) + 10,
             (55 * self.nb_lignes) + 10,
             text = texte, font = 'Calibri 40', fill = 'white')

    def carte_selectionnee(self, event):
        """Fonction qui permet de bien choisir la carte selectioné"""
        #La méthode find_closest() renvoie le numéro de la carte la plus
        #proche des coordonnées de la souris au moment du clic. Le résultat
        #sera un tuple. Par exemple, le résultat (2,) indiquera la carte no2
        #L'identifiant de la carte sera donc le premier élément du tuple.
        if len(self.cartes_jouees) < 2:
            carteSel = self.canvas.find_closest(event.x, event.y)
            carteID = carteSel[0]

            if self.fini:
                self.fini = False
                self.reinitialiser()
            else:
                # montre la carte, carteID = numero de la carte
                self.canvas.itemconfig(
                    carteID, image = self.images[self.cartes[carteID - 1]])
                # enregistre la carte jouée
                if len(self.cartes_jouees) == 0:
                    # permet de ne pas cliquer 2x sur la même carte
                    self.cartes_jouees.append(carteID)
                elif carteID != self.cartes_jouees[0]:
                    self.cartes_jouees.append(carteID)
        if self.peut_jouer and len(self.cartes_jouees) == 2:
            self.peut_jouer = False
            # désactive l'effet du clic de la souris
            self.frame.after(1500, self.tirage)
            # patiente 1,5 secondes avant de continuer

    def menus_memory(self, fen):
        """ Fonction qui s'occupe du menu du memory"""
        #l'onglet options est en haut
        top = Menu(fen)
        fen.config(menu = top)

        jeu = Menu(top, tearoff = False)
        top.add_cascade(label = 'Options', menu = jeu)
        jeu.add_command(label = 'Nouvelle partie', command = self.reinitialiser)
        jeu.add_command(label = 'Quitter', command = self.callbackExit)

    def canevas(self, fen, col, lig):
        """Fonction de la zone rectangulaire destinée à contenir les images et
         les cartes"""
        #les dimensiosn et les couleurs
        return Canvas(fen, width = (110 * col) + 10, height = (110 * lig) + 10,
        bg = 'white')

    def reinitialiser(self):
        """Fonction qui fait que la partie recommence"""
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
        self.canvas = self.canevas(
            self.frame, self.nb_colonnes, self.nb_lignes)
        self.canvas.pack(side = TOP, padx = 2, pady = 2)
        self.points_joueur1 = Label(self.frame, text = "Player 1 : 0",
                                    bg = "lightcoral", font = "Comic 16")
        self.points_joueur1.pack(pady = 2, side = LEFT)
        self.points_joueur2 = Label(
            self.frame, text = "Player 2 : 0", bg = "white", font = "Comic 16")
        self.points_joueur2.pack(pady = 2, side = RIGHT)
        self.images_chargement()
        self.cartes_melanges()
        for i in range(self.nb_colonnes):
            # dessin des cartes retournées
            for j in range(self.nb_lignes):
                self.canvas.create_image(
                    (110 * i) + 60, (110 * j) + 60, image = self.images[0])
        # permet le clic sur les cartes
        self.canvas.bind("<Button - 1>", self.carte_selectionnee)

    def createFrame(self, window, callbackExit):
        """ Ce qui permet d'inserer le memory dans le bouton de l'interface"""
        self.callbackExit = callbackExit
        self.frame = Frame(window)
        self.frame.pack()
        self.menus_memory(window)
        self.reinitialiser()
        return self.frame