from tkinter import Tk, DoubleVar, Canvas, Button, BOTH, YES, Frame, SE
from functools import partial
import random
from tkinter.constants import ANCHOR, CENTER
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
        """ returns list with values on square to compare with when generating,
        it finds out square and first index in that square. Looping through all the those values and adding them to list and returning that value.
        """  
        
        lst = []
        square = (index % 9 // 3) + (index // 27 * 3)
        start_lst = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        start = start_lst[square]
        
        # Subsquare index, counts:
        # 0,9,18...1,10,19 etc.
        for move in range(3):
            end = start + move + 19
            [lst.append(value) for value in range(start + move, end, 9)]
            
        return [root.getvar(str(num)) for num in lst]


class RemoveNumbers:
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
        self.instantAnimation = False
        self.data = data
        self.root = root

        # Must do
        root.resizable(False, False)
        root.update()
        print(root.winfo_height())
        
        # Canvas for background
        self.bg = Canvas(root, bg='gray', height=root.winfo_height(), width=root.winfo_width())

        root.update()
        print(root.winfo_height()-20)
        # Canvas for grid
        self.grid = Canvas(self.bg, bg='black', width=(
            root.winfo_height()-20), height=(root.winfo_height()-20),highlightthickness=0)

        # Good ones
        self.bg.pack(fill=BOTH, expand=YES)
        self.grid.place(x=20, y=20)

        # If true, numbers will render instant
        self.small_frames()
        self.button_frames()
        self.makeButtons()
        #self.renderButtons()
        
        root.resizable(True, True)
        #self.bg.bind('<Configure>', self.onResize)

    def small_frames(self):
        #Working
        self.canvaslst = []
        
        root.update()
        for index in range(9):
            self.canvaslst.append(Frame(self.grid, highlightthickness=0, width=self.grid.winfo_height()/3, height=self.grid.winfo_height()/3, bg='black'))

            self.canvaslst[index].grid(row=int(index/3), column=int(index%3),padx=1, pady=1, sticky='ns')
    
    def button_frames(self):
        self.button_canvas_lst = []
        
        root.update()
        for index in range(81):
            square = (index % 9 // 3) + (index // 27 * 3)
            self.button_canvas_lst.append(Canvas(self.canvaslst[square], highlightthickness=0, width=self.canvaslst[0].winfo_height()/3, height=self.canvaslst[0].winfo_height()/3, bg='white'))
            
            self.button_canvas_lst[index].grid(row=int(index/3), column=int(index%3),padx=1, pady=1, sticky='ns')
                    
    def makeButtons(self):
        size = self.canvaslst[0].winfo_height()/3
        for index in range(81):
                        
            # Button information
            self.data.buttons.append(
                Button(self.button_canvas_lst[index], name=str(index), font=('consolas', 18, 'bold'), relief='flat', bg='white', bd=0, activebackground='white', command=partial(self.triggerEditting, index)))

            self.data.buttons[index].place(x=0, y=0, height=size, width=size)
        root.update()
            

    def renderButtons(self):
        for index, button in enumerate(self.data.buttons):
            button['text'] = self.root.getvar(str(index))

            # Render one by a time
            if self.instantAnimation == False:
                root.update()
                root.after(25)
        
        #Instant board
        root.update()

    def onResize(self, event):
        minSize = min(event.width, event.height) - 40
        self.grid.config(width=minSize, height=minSize)

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
        self.removeNum = RemoveNumbers(root, self.data)
        self.multiplayer = Multiplayer(root, self.data)
        self.board = Board(root, self.data)
        keyboard.on_press(self.keyboardPress)

    # Runs when keyboard button is pressed
    def keyboardPress(self, event):
        
        # If 1 to 9 is pressed
        # Sends key to changeNumber
        if event.name.isdigit() and int(event.name) in self.data.possible_numbers and self.data.editting_now != None:
            self.board.changeNumber(int(event.name))

        # Allows the player to empty a square
        elif event.name == 'backspace':
            self.board.changeNumber('')

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
root.title('Sudoku Game')
root.geometry('1920x1080')
root.state('normal')

#May not works
root.iconbitmap('')

game = Game(root)
root.mainloop()
