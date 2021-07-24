from tkinter import Tk, IntVar, Canvas, BOTH, YES, Button, font
import random


class DataBase:
    def __init__(self, root):
        self.validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.boardAnswer = []
        self.button = []
        self.lines = []
        self.data = []

        # Generating empty varibles
        for index in range(81):
            self.data.append(IntVar(root, name=str(index)))

        # Start generating
        self.numberGenerator()

    def numberGenerator(self):

        loop = True
        index = 0
        while loop:

            # Pinch of randomness
            # Todo make generating with a seed
            # Todo make generating with traceback method
            random.shuffle(self.validNumbers)

            tempRow = self.getRowFor(index, True)
            tempColumn = self.getColumnFor(index, True)
            tempSquare = self.getSquareFor(index, True)

            for count, num in enumerate(self.validNumbers):

                check = True
                # Is it valid to place number or not
                if num in tempRow or num in tempColumn or num in tempSquare:
                    check = False

                # If okay to set value
                if check == True:
                    # Sets value in the dataBase
                    root.setvar(name=str(index), value=num)
                    index += 1
                    break

                # If row on gameboard fails to generate
                if (count + 1) == 9:

                    # Clears all values on board
                    for tempIndex in range(81):
                        root.setvar(name=str(tempIndex), value=0)

                    index = 0
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
        # Vars
        self.data = data
        self.root = root
        self.scale = 100/9-11

        # Canvas
        self.background = Canvas(
            root, bg="gray", height=root.winfo_height(), width=root.winfo_width())

        self.grid = Canvas(self.background, bg="white", width=(
            root.winfo_height()-40), height=(root.winfo_height()-40))

        # Lines
        self.renderLines()
        for index in range(3, len(self.data.lines), 3):
            # Make thick lines
            self.grid.itemconfig(self.data.lines[index], width=2)

        # Update and render
        self.background.bind("<Configure>", self.onResize)
        self.background.pack(fill=BOTH, expand=YES)
        self.grid.place(x=20, y=20)

        # If true, numbers will render instant
        self.renderNumbers(root, True)
        root.update()

    def onResize(self, event):
        minSize = min(event.width, event.height) - 40

        # Canvas
        self.grid.config(width=minSize, height=minSize)

        # Lines
        # ? Shorten the cordinates
        for index in range(18):
            # Horizontal lines
            if index <= 8:
                self.grid.coords(
                    self.data.lines[index], 0, (minSize*(self.scale*index)), minSize, (minSize*(self.scale*index)))

            # Vertical line
            else:
                self.grid.coords(
                    self.data.lines[index], (minSize*(self.scale*(index-9))), 0,  (minSize*(self.scale*(index-9))), minSize)

        # Buttons
        size = (minSize/9) - 3
        yCord = 2
        count = 0

        # ? Shorten the for loop
        for index in range(81):
            if index % 9 == 0 and index != 0:
                yCord += minSize/9
                count = 0

            # Update button place
            self.data.button[index].place(
                x=2+(count*(minSize/9)), y=yCord, width=size, height=size)

            # Update number font/size
            self.data.button[index].configure(
                font=("consolas", int(minSize/9*0.4), "bold"))

            count += 1

    def renderNumbers(self, root, renderInstant):
        yCord = 2
        count = 0

        for index in range(81):
            # Button information
            self.data.button.append(
                Button(self.grid, name=str(index), font=(
                    "consolas", 18, "bold"), relief="flat", bg="white", activebackground='white', bd=0)
            )

            # Frame Cordinates
            if index % 9 == 0 and index != 0:
                yCord += 45
                count = 0

            self.data.button[index].place(
                x=2+(count*45), y=yCord, width=42, height=42)

            # Animate numbers
            self.data.button[index]["text"] = root.getvar(str(index))

            if renderInstant == False:
                root.update()
                root.after(20)

            count += 1

        # Instant render
        if renderInstant == True:
            root.update()

    def renderLines(self):
        for _ in range(18):

            # Makes all lines
            # Cordinates updates imidetly inside
            # onRezise, no need to be exact
            self.data.lines.append(self.grid.create_line(0, 41, 396, 41))


class Game:
    def __init__(self, root):
        self.data = DataBase(root)
        self.board = RenderBoard(root, self.data)


# Game window properties
root = Tk()
root.title("Soduko Game")
root.geometry("608x446")

print("loading....")
game = Game(root)
root.mainloop()
