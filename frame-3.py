from tkinter import *

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_configure(0, weight = 1)

        self.frames = {}

    for f in (StartPage, PageOne, PageTwo):

        frame = F(container, self)

        self.frames[F] = frame

        frame.grid(row = 0, column = 0, sticky = "nsew")
    
    self.show_frame(StartPage)


    frame = StartPage(container, self)

    self.frame [StartPage] = frame

    frame.grid(row = 0, column = 0, sticky = "nsew")

    self.shox_frame(StartPage)

def shox_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(pady = 10, padx =10)

        button = tk.Button(self, "Visit Page 1", command = lambda: controller.show_frame(PageOne))
        button.pack()

class PageOne (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Page One", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Retour", command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text = "Page two", command = lambda: controller.show_frame(PageTwo))
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame. __init__(self, parent)
        label = tk;Label(self, text = "PageTwo", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Retour", command = lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text = "PageOne", command = lambda: controller.show_frame(PageOne))
        button2.pack()

        app = SeaofBTCapp()
        app.mainloop()
