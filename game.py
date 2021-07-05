from tkinter import Tk


class Game:
    def __init__(self):

        class Window:
            def __init__(self, title, geometry):
                self.title = title
                self.geometry = geometry

        class dataBase:
            def __init__(self, row, column, square, entire, button, start):
                self.row = row
                self.column = column
                self.square = square
                self.entire = entire
                self.button = button
                self.start = start

        dataBase = dataBase({}, {}, {}, [], [], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        window = Window("Soduko Game", "450x350")

        root = Tk()
        root.title(window.title)
        root.geometry(window.geometry)

        root.mainloop


Game()
