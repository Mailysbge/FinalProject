from tkinter import *


joueur = 0


class jeuMorpion:
    def Clic(event):
        """ Gestion de l'événement Clic gauche sur la zone graphique """
        # position du pointeur de la souris
        X = event.x
        Y = event.y
        print(X, Y)
        if 1 <= X <= 183 :
            colonne = 1
        elif 184 <= X <= 366 :
            colonne = 2
        elif 367 <= X <= 550 :
            colonne = 3
        if 1 <= Y <= 183 :
            ligne = 1
        elif 184 <= Y <= 366 :
            ligne = 2
        elif 367 <= Y <= 550 :
            ligne = 3
        nombre_case = ligne*3+(colonne-3)
        print (nombre_case)
        if nombre_case == 1 and joueur % 2 == 0:
            item = Canevas.create_image(12, 12,anchor=NW, image=croix)

        elif nombre_case == 2 and joueur%2 == 0:
            item = Canevas.create_image(196, 12,anchor=NW, image=croix)

        elif nombre_case == 3 and joueur%2 == 0:
            item = Canevas.create_image(380, 12,anchor=NW, image=croix)

        elif nombre_case == 4 and joueur%2 == 0:
            item = Canevas.create_image(12, 196,anchor=NW, image=croix)

        elif nombre_case == 5 and joueur%2 == 0:
            item = Canevas.create_image(196, 196,anchor=NW, image=croix)

        elif nombre_case == 6 and joueur%2 == 0:
            item = Canevas.create_image(380, 196,anchor=NW, image=croix)

        elif nombre_case == 7 and joueur%2 == 0:
            item = Canevas.create_image(12, 380,anchor=NW, image=croix)

        elif nombre_case == 8 and joueur%2 == 0:
            item = Canevas.create_image(196, 380,anchor=NW, image=croix)

        elif nombre_case == 9 and joueur%2 == 0:
            item = Canevas.create_image(380, 380,anchor=NW, image=croix)

        elif nombre_case == 1 and joueur % 2 == 1:
            item = Canevas.create_image(12, 12,anchor = NW, image = cercle)

        elif nombre_case == 2 and joueur%2 == 1:
            item = Canevas.create_image(196, 12,anchor = NW, image = cercle)

        elif nombre_case == 3 and joueur%2 == 1:
            item = Canevas.create_image(380, 12,anchor = NW, image = cercle)

        elif nombre_case == 4 and joueur%2 == 1:
            item = Canevas.create_image(12, 196,anchor = NW, image = cercle)

        elif nombre_case == 5 and joueur%2 == 1:
            item = Canevas.create_image(196, 196,anchor = NW, image = cercle)

        elif nombre_case == 6 and joueur%2 == 1:
            item = Canevas.create_image(380, 196,anchor = NW, image = cercle)

        elif nombre_case == 7 and joueur%2 == 1:
            item = Canevas.create_image(12, 380,anchor = NW, image = cercle)

        elif nombre_case == 8 and joueur%2 == 1:
            item = Canevas.create_image(196, 380,anchor = NW, image = cercle)

        elif nombre_case == 9 and joueur%2 == 1:
            item = Canevas.create_image(380, 380,anchor = NW, image = cercle)
        joueur = joueur+1
        global joueur



    # Création de la fenêtre principale (main window)
    Mafenetre = Tk()
    Mafenetre.title('Morpion')
    #image du cercle
    cercle = PhotoImage(file="cercle.png")
    #image de la croix
    croix = PhotoImage(file="croix.png")
    # Image de fond
    photo = PhotoImage(file="quadrillage.png")
    # Création d'un widget Canvas (zone graphique)
    Largeur = 550
    Hauteur = 550
    Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
    item = Canevas.create_image(2,2,anchor=NW, image=photo)
    print("Image defond (item",item,")")
    Canevas.pack()


    Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
    Bouton1.pack()
    Canevas.bind('<Button-1>', Clic)
    Canevas.pack(padx =5, pady =5)

    Mafenetre.mainloop()