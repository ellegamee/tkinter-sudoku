from tkinter import Tk, IntVar
import random


class DataBase:
    def __init__(self, root):
        self.validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.boardAnswer = []
        self.button = []
        self.data = []

        # Empty varibles
        for index in range(81):
            self.data.append(IntVar(root, name=str(index)))

        self.numberGenerator()

    def numberGenerator(self):
        loop = True
        index = 0
        while loop:

            random.shuffle(self.validNumbers)
            for count, num in enumerate(self.validNumbers):

                check = True
                if num in self.getRowFor(index, True) or num in self.getColumnFor(index, True) or num in self.getSquareFor(index, True):
                    check = False

                if check == True:
                    root.setvar(name=str(index), value=num)
                    index += 1
                    print("num", num)
                    print("index", index)
                    break

                if (count + 1) == 9:
                    print("test")
                    index = self.getRowFor(index, False)[0]

                    for tempIndex in self.getRowFor(index, False):
                        root.setvar(name=str(tempIndex), value=0)

                    break

            if index == 81:
                loop = False

        # * Makes copy of entire grid
        for index in range(81):
            self.boardAnswer.append(root.getvar(str(index)))

    def getRowFor(self, index, convertToValue):
        start = index // 9 * 9

        if convertToValue == True:
            lstReturn = []
            for i in range(start, (start + 9)):
                lstReturn.append(root.getvar(str(i)))
            return lstReturn

        else:
            return list(range(start, (start + 9)))

    def getColumnFor(self, index, convertToValue):
        start = index % 9

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
            for _ in range(3):
                for value in range(start, end+1, 9):
                    lst[listKey].append(value)

                start += 1
                end += 1

            if listKey == 2 or listKey == 5:
                start += 18
                end += 18

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


root = Tk()
root.title("Soduko Game")
root.geometry("450x350")

game = Game(root)
print(game.data.boardAnswer)

root.mainloop()
