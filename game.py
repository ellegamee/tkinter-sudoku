from tkinter import Tk, IntVar
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

        # * Makes all lists
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


class Game:
    def __init__(self, root):
        self.data = DataBase(root)
        self.generateGameBoard()

    def generateGameBoard(self):
        for index in range(81):
            # Button information
            # ? Make button something else
            self.data.button.append(
                Button(
                    root,
                    name=f"b{index}",
                    style="TButton",
                )
            )

            # Row and column to put button
            row = index // 9 * 9
            column = index % 9 * 9
            self.data.button[index].grid(row=row, column=column)

        # Transition animation when loading
        for i in range(81):
            self.data.button[i]["text"] = root.getvar(f"{i}")
            root.update()
            root.after(20)


# Game window properties
root = Tk()
style = Style()
root.title("Soduko Game")
root.geometry("450x350")

style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

game = Game(root)
print(game.data.boardAnswer)

root.mainloop()
