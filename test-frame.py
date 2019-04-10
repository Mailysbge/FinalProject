from tkinter import *

root = Tk()
frames = [ Frame(root, width=100, height=100, bg=color) for color in ('red', 'green', 'blue')]
index = 0
frames[index].grid(row=0)

def show_next():
     global index
     frames[index].grid_forget()
     index = (index + 1) % len(frames)
     frames[index].grid(row=0)
    
Button(root, text='next', command=show_next).grid(row=1)

show_next()