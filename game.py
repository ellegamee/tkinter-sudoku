from tkinter import Tk


class Game:
    def __init__(self):
        pass


class Window:
    def __init__(self, title, geometry):
        self.title = title
        self.geometry = geometry


window = Window("Soduko Game", "450x350")

root = Tk()
root.title(window.title)
root.geometry(window.geometry)
