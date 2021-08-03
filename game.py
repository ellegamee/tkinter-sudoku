from tkinter import Tk, DoubleVar, Canvas, Button, BOTH, YES
from functools import partial
import random
import keyboard
import requests


class Database:
    def __init__(self, root):
        self.data = [DoubleVar(root, name=str(index)) for index in range(81)]
        self.possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.editting_now = None
        self.buttons = []
        self.lines = []

        # Start generating
        self.generate_numbers()
        self.board_answer = [root.getvar(str(index)) for index in range(81)]

    def generate_numbers(self):
        ''' takes and generates all numbers for a game
        by using row_nums, column_nums and square_nums
        wich a random number is compared to and makes
        in the end a full board
        '''

        loop = True
        index = 0
        while loop:
            # Pinch of randomness needed for it to work
            random.shuffle(self.possible_numbers)

            # ? Able to shorten/improve
            numbers = self.row_nums(index) + self.column_nums(
                index) + self.square_nums(index)

            for count, num in enumerate(self.possible_numbers):
                # If number is allowd to get put
                if num not in numbers:
                    root.setvar(name=str(index), value=num)
                    index += 1
                    break

                # If row on gameboard fails to generate
                # ? Push this in one tab
                if count == 8:

                    # Clears all values on board to 0
                    for varible in self.data:
                        varible.set(0)

                    index = 0
                    break

            if index == 81:
                loop = False

    def row_nums(self, index):
        """ returns list with values on row to compare with"""
        start = index // 9 * 9
        return [root.getvar(str(i)) for i in range(start, (start + 9))]

    def column_nums(self, index):
        """ returns list with values on column to compare with"""
        start = index % 9
        return [root.getvar(str(i)) for i in range(start, (start + 9*9), 9)]

    def square_nums(self, index):
        """ returns list with values on square to compare with
        r = row
        c = column
        """

        lst = [[], [], [], [], [], [], [], [], []]
        r = index // 9
        c = index % 9
        start = 0
        end = 18

        # Makes all lists
        # ! THREE FOR LOOPS INSIDE EACH OTHER?!
        # TODO Search for improvement with the loops
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

        return [root.getvar(str(i)) for i in lst[((c // 3) + (r // 3 * 3))]]


class RemoveNumbers:
    #! Value on the empty buttons is strings
    #! And not ints as the rest of the buttons

    # Todo Totally random and makes NON-unique
    # Todo solutions, needs and improvement

    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.removed = 0

        while self.removed <= (81 - 34):
            index = random.randrange(81)

            # Check if button is already empty
            if root.getvar(str(index)) == None:
                continue

            # Changes the value to empty
            root.setvar(str(index), value="")
            self.removed += 1
            continue


class Board:
    def __init__(self, root, data):
        # Vars
        self.instantAnimation = True
        self.data = data
        self.root = root

        # Must do
        root.resizable(False, False)
        root.update()

        # Canvas for background
        self.bg = Canvas(
            root, bg='gray', height=root.winfo_height(), width=root.winfo_width())

        # Canvas for grid
        self.grid = Canvas(self.bg, bg='white', width=(
            root.winfo_height()-40), height=(root.winfo_height()-40))

        # Makes lines and everythird is 2px thick
        self.data.lines = [self.grid.create_line(
            0, 0, 0, 0) for _ in range(18)]

        for line in [i for i in range(18) if i % 3 == 0]:
            self.grid.itemconfig(self.data.lines[line], width=2)

        # Good ones
        self.bg.pack(fill=BOTH, expand=YES)
        self.grid.place(x=20, y=20)
        self.lineCordinates()

        # If true, numbers will render instant
        self.makeButtons()
        self.renderButtons()

        root.resizable(True, True)
        self.bg.bind('<Configure>', self.onResize)

    def lineCordinates(self):
        scale = 100/9-11
        minSize = min(self.root.winfo_height()-40, self.root.winfo_width()-40)

        for index in range(18):
            # Horizontal lines
            if index <= 8:
                self.grid.coords(
                    self.data.lines[index], 0, (minSize*(scale*index)), minSize, (minSize*(scale*index)))

            # Vertical line
            else:
                self.grid.coords(
                    self.data.lines[index], (minSize*(scale*(index-9))), 0,  (minSize*(scale*(index-9))), minSize)

    def makeButtons(self):
        for index in range(81):
            # Button information
            self.data.buttons.append(
                Button(self.grid, name=str(index), font=('consolas', 18, 'bold'), relief='flat',
                       bg='white', bd=0, activebackground='white', command=partial(self.triggerEditting, index))
            )

            # Update the text on the button from Database
            self.data.buttons[index]['text'] = self.root.getvar(str(index))

    def renderButtons(self):
        yCord = 2
        count = 0

        for index, button in enumerate(self.data.buttons):
            if button != "":

                # Button Cordinates
                if index % 9 == 0 and index != 0:
                    yCord += 45
                    count = 0

                xCord = 2+(count*45)
                button.place(x=xCord, y=yCord, width=42, height=42)
                count += 1

                # Render one by a time
                if self.instantAnimation == False:
                    root.update()
                    root.after(25)

                # Render instant
                elif self.instantAnimation == True and index == 81:
                    root.update()

    def onResize(self, event):
        minSize = min(event.width, event.height) - 40
        self.grid.config(width=minSize, height=minSize)
        self.lineCordinates()

        # Buttons
        size = (minSize/9) - 3
        yCord = 2
        count = 0

        for index, button in enumerate(self.data.buttons):
            if index % 9 == 0 and index != 0:
                yCord += minSize/9
                count = 0

            # Vars for button update
            xCord = 2+(count*(minSize/9))
            fontSize = int(minSize/9*0.4)

            # Updates button place/config
            button.place(x=xCord, y=yCord, width=size, height=size)
            button.configure(font=('consolas', fontSize, 'bold'))

            count += 1

    # TODO Change position, place it in game or new class
    # TODO Maybe inside game even, need index to be global
    def triggerEditting(self, index):
        # When button is not pressed
        if self.data.editting_now == None:
            self.data.editting_now = [index]
            self.data.buttons[index].configure(bg='lightgray')

        # Multiselection buttons
        elif keyboard.is_pressed('ctrl'):
            self.data.buttons[index].configure(bg='lightgray')

            # If the button is not in edit list
            if index not in self.data.editting_now:
                self.data.editting_now.append(index)

        # Previous button still toggeld
        else:
            for editIndex in self.data.editting_now:
                self.data.buttons[editIndex].configure(bg='white')
                self.data.editting_now = [index]
                self.data.buttons[index].configure(bg='lightgray')

    def changeNumber(self, key):
        print('keyboard:', key)
        print(f'index button: {self.data.editting_now}\n')

        for editIndex in self.data.editting_now:
            # Changing the number in Database and on button
            self.data.data[editIndex].set(key)
            self.data.buttons[editIndex]['text'] = key

            # Deselecting button after new number is placed
            self.data.buttons[editIndex].configure(bg='white')
            self.data.editting_now = None


class Multiplayer():
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.pushToCloudflare()

    def pushToCloudflare(self):
        gameBoard = requests.put('https://sodukokv.axonov.workers.dev/test',
                                 json=[root.getvar(str(index)) for index in range(81)])
        print(f'cloudflare: {gameBoard}')

    def getFromCloudflare(self):
        gameBoard = requests.get('https://sodukokv.axonov.workers.dev/test')
        print(gameBoard)


class Game:
    def __init__(self, root):
        self.data = Database(root)
        #self.removeNum = RemoveNumbers(root, self.data)
        self.multiplayer = Multiplayer(root, self.data)
        self.board = Board(root, self.data)
        keyboard.on_press(self.keyboardPress)

    # Runs when keyboard button is pressed
    def keyboardPress(self, event):

        # If 1 to 9 is pressed
        # Sends key to changeNumber
        if event.name.isdigit() and int(event.name) in self.data.possible_numbers and self.data.editting_now != None:
            self.board.changeNumber(int(event.name))

        # Clears all selected squares
        elif event.name == 'esc':
            for editIndex in self.data.editting_now:
                self.data.buttons[editIndex].configure(bg='white')

            self.data.editting_now = None

        # Quits program
        elif event.name == 'q':
            root.destroy()


# Game window properties
root = Tk()
root.title('Soduko Game')
root.geometry('608x446')

game = Game(root)
root.mainloop()
