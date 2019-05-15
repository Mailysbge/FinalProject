from tkinter import *

class Menu:
    def createFrame(self, window, callbackMemoryClick, callbackPingPongClick, callbackMorpionClick):
        frame = Frame(window)
        frame.pack()
        # Création d'un widget Button (bouton mémorie) 
        memoryButton = Button(frame, text ='Memory', command = callbackMemoryClick) 
        # Positionnement du widget avec la méthode pack() 
        memoryButton.pack(side = LEFT, padx = 140, pady = 150) 
        
        # Création d'un widget Button (bouton Ping-pong) 
        pingPongButton = Button(frame, text ='Dan-Du', command = callbackPingPongClick) 
        pingPongButton.pack(side = LEFT, padx = 100, pady = 150)

        # Création d'un widget Button (bouton Morpion) 
        MorpionButton = Button(frame, text ='Morpion', command = callbackMorpionClick) 
        MorpionButton.pack(side = LEFT, padx = 100, pady = 150)

        return frame