from tkinter import *

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Frame widget')
Mafenetre['bg']='bisque' # couleur de fond

# création d'un widget Frame dans la fenêtre principale
Frame1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT,padx=10,pady=10)

# création d'un second widget Frame dans la fenêtre principale
Frame2 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
Frame2.pack(side=LEFT,padx=10,pady=10)

# création d'un widget Button dans un widget Frame
Button(Frame1,text="Memory",fg='navy',command=Frame1.destroy).pack(padx=10,pady=10)

Button(Frame2,text="Dan",fg='navy',command=Frame2.destroy).pack(padx=10,pady=10)


Mafenetre.mainloop()