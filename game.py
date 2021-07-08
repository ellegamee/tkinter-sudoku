from tkinter import Tk, IntVar, Canvas, TOP
from tkinter.ttk import Button, Style
import random


class DataBase:
    def __init__(self, root):
        self.validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.boardAnswer = []
        self.button = []
        self.data = []

        # Generating empty varibles
        for index in range(81):
            self.data.append(IntVar(root, name=str(index)))

        self.numberGenerator()

    def numberGenerator(self):
        loop = True
        index = 0
        while loop:

            # Pinch of randomness
            # Todo make generating with a seed
            random.shuffle(self.validNumbers)
            for count, num in enumerate(self.validNumbers):

                check = True
                # Is it valid to place number or not
                if num in self.getRowFor(index, True) or num in self.getColumnFor(index, True) or num in self.getSquareFor(index, True):
                    check = False

                # If okay to set value
                if check == True:
                    # Sets value in the dataBase
                    root.setvar(name=str(index), value=num)
                    index += 1
                    break

                # If row on gameboard fails to generate
                if (count + 1) == 9:
                    # Backs index back to start of row
                    index = self.getRowFor(index, False)[0]

                    # Clears all values on row
                    for tempIndex in self.getRowFor(index, False):
                        root.setvar(name=str(tempIndex), value=0)

                    break

            if index == 81:
                loop = False

        # Makes the answer sheet for the game
        for index in range(81):
            self.boardAnswer.append(root.getvar(str(index)))

    def getRowFor(self, index, convertToValue):
        start = index // 9 * 9

        # Return scenarios
        if convertToValue == True:
            lstReturn = []
            for i in range(start, (start + 9)):
                lstReturn.append(root.getvar(str(i)))
            return lstReturn

        else:
            return list(range(start, (start + 9)))

    def getColumnFor(self, index, convertToValue):
        start = index % 9

        # Return scenarios
        if convertToValue == True:
            lstReturn = []
            for i in range(start, (start + 9*9), 9):
                lstReturn.append(root.getvar(str(i)))
            return lstReturn

        else:
            return list(range(start, (start + 9*9), 9))

    def getSquareFor(self, index, convertToValue):
        row = index // 9
        column = index % 9

        lst = [[], [], [], [], [], [], [], [], []]
        start = 0
        end = 18

        # Makes all lists
        for listKey in range(9):

            # Subsquare index, counts:
            # 0,9,18...1,10,19 etc.
            for _ in range(3):
                for value in range(start, end+1, 9):
                    lst[listKey].append(value)

                # Move start to next index
                start += 1
                end += 1

            # When first 3 or 6 subsquares are done
            if listKey == 2 or listKey == 5:
                start += 18
                end += 18

        # Return scenarios
        if convertToValue == True:
            lstReturn = []
            for i in lst[((column // 3) + (row // 3 * 3))]:
                lstReturn.append(root.getvar(str(i)))
            return lstReturn

        else:
            return lst[((column // 3) + (row // 3 * 3))]


class RenderBoard:
    def __init__(self, root, data):
        self.data = data
        self.renderNumbers(root)

        while True:
            self.renderGrid(root)

    def renderNumbers(self, root):
        for index in range(81):
            # Button information
            self.data.button.append(
                Button(root, name=str(index), style="TButton")
            )

            # Where to put button
            self.data.button[index].place(x=20, y=20)

            # Animation numbers
            self.data.button[index]["text"] = root.getvar(str(index))
            root.update()
            root.after(20)

    def renderGrid(self, root):
        grid = Canvas(root, bg="blue", width=root.winfo_width(),
                      height=root.winfo_height())

        grid.place(x=-1, y=-1)
        root.update()


class Game:
    def __init__(self, root):
        self.data = DataBase(root)
        self.board = RenderBoard(root, self.data)


# Game window properties
root = Tk()
style = Style()
root.title("Soduko Game")
root.geometry("450x350")

style.configure("TButton", font=("calibri", 15, "bold"),
                height=10, width=3, relief="flat")

game = Game(root)
root.mainloop()
