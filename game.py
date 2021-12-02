from tkinter import PhotoImage, Tk, DoubleVar, Canvas, Button, BOTH, YES, Frame, Label, font, ttk, CENTER
from functools import partial
import random
import keyboard
import requests
import platform

class Database:
    def __init__(self, root):
        self.data = [DoubleVar(root, name=str(index)) for index in range(81)]
        self.possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.editting_now = []
        self.buttons = []
            
    def make_database(self):
        self.generate_numbers()
        self.board_answer = [root.getvar(str(index)) for index in range(81)]
        
    def reset_database(self):
        for item in self.data:
            item.set('')

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
    
    def remove_numbers(self):
        removed = 0
        empty = 0
        
        while removed <= (81 - 34):
            index = random.randrange(81)
    
            # Check if button is already empty
            if root.getvar(str(index)) == "":
                empty += 1
            
            previos_value = root.getvar(str(index))
            root.setvar(str(index), value="")
            
            numbers = self.row_nums(index) + self.column_nums(
                index) + self.square_nums(index)
            
            solutions = 0
            for num in self.possible_numbers:
                if num not in numbers:
                    solutions += 1
            
            if solutions > 1:
                root.setvar(str(index), value=previos_value)
                continue
            
            else:
                removed += 1
                continue
                    
class Board:
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.main_menu()

    def createBoard(self):
          # Vars
        self.instantAnimation = True

        # Must do
        #root.resizable(False, False)
        root.update()
        
        # Canvas for background
        self.bg = Canvas(root, bg='gray', height=root.winfo_height(), width=root.winfo_width())

        root.update()
        # Canvas for grid
        self.grid = Canvas(self.bg, bg='black', width=(
            root.winfo_height()-400), height=(root.winfo_height()-400),highlightthickness=0)

        # Good ones
        self.bg.pack(fill=BOTH, expand=YES)
        self.grid.place(x=20, y=20)

        # If true, numbers will render instant
        self.small_frames()
        self.button_frames()
        self.makeButtons()
        self.renderButtons()
        self.orginial_numbers()
        
        #root.resizable(True, True)

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
                Button(self.button_canvas_lst[index], name=str(index), font=('consolas', 24, 'bold'), relief='flat', bg='white', bd=0, activebackground='white', command=partial(self.triggerEditting, index)))

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
            
    def triggerEditting(self, index):
        # When button is not pressed
        if self.data.editting_now == []:
            self.data.editting_now = [index]
            self.data.buttons[index].configure(bg='lightgray')

        # Multiselection buttons
        elif keyboard.is_pressed('ctrl'):
            self.data.buttons[index].configure(bg='lightgray')

            # If the button is not in edit list
            if index not in self.data.editting_now:
                self.data.editting_now.append(index)
     
        # Deselects old buttons when new button is clicked 
        else:
            
            if index in self.data.editting_now:
                self.data.editting_now = []
                self.data.buttons[index].configure(bg='white')

            else:    
                for editIndex in self.data.editting_now:
                    self.data.buttons[editIndex].configure(bg='white')
                    self.data.editting_now = [index]
                    self.data.buttons[index].configure(bg='lightgray')
        
    def changeNumber(self, key):
        for editIndex in self.data.editting_now:
            # Changing the number in Database and on button
            self.data.data[editIndex].set(key)
            self.data.buttons[editIndex]['text'] = key

            # Deselecting button after new number is placed
            self.data.buttons[editIndex].configure(bg='white')
            self.data.editting_now = []
    
    def  orginial_numbers(self):
        for index in range(81):
            self.data.buttons[index].configure(fg='black')
            
            if type(root.getvar(name=f'{index}')) == int:
                self.data.buttons[index].configure(fg='blue')
    
    def win_dialog(self):
        self.win_frame = Frame(self.bg)
        text = Label(self.win_frame, text="Congrats you won!\nPlay again?", font=("Franklin Gothic Medium", 33))
        text.place(relx=0.5, rely=0.3, anchor=CENTER, relheight=0.45, relwidth=0.8)
        
        b_menu = ttk.Button(self.win_frame, text="Main menu", command=self.removeBoard, style='win_b.TButton', takefocus=False)
        b_retry = ttk.Button(self.win_frame, text="Retry", command=self.retry, style='win_b.TButton', takefocus=False)
        self.style.configure('win_b.TButton', font=("Franklin Gothic Medium", 20))
        b_menu.place(relx=0.75, rely=0.75, relheight=0.3, relwidth=0.4, anchor=CENTER)
        b_retry.place(relx=0.25, rely=0.75, relheight=0.3, relwidth=0.4, anchor=CENTER)

        
        self.win_frame.configure(borderwidth=2, relief="solid")
        self.win_frame.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.3, anchor=CENTER)

    def removeBoard(self):
        for child in self.bg.winfo_children():
            child.destroy()
        self.bg.destroy()
    
    def retry(self):
        self.data.reset_database()
        self.data.make_database()
        
        self.data.remove_numbers()
        self.win_frame.destroy()
        self.orginial_numbers()
        self.renderButtons()
    
    def pressPlay(self):
        self.data.buttons = []
        self.data.reset_database()
        self.data.make_database()
        self.data.remove_numbers()
        self.createBoard()
        
    
    def pressExit(self,root):
        root.destroy()
    
    def main_menu(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.t_heading = Label(self.root, text='SUDOKU')
        self.t_heading.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.b_play = ttk.Button(self.root, text="Play", takefocus=False, command=(self.pressPlay))
        self.b_play.place(relx=0.5, rely=0.45, relwidth=0.2, relheight=0.11, anchor=CENTER)

        self.b_test = ttk.Button(self.root, text='Test', takefocus=False)
        self.b_test.place(relx=0.5, rely=0.60, relwidth=0.2, relheight=0.11, anchor=CENTER)

        self.b_exit = ttk.Button(self.root, text='Exit', takefocus=False, command=partial(self.pressExit,root))
        self.b_exit.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.11, anchor=CENTER)

        self.style.configure('TButton', font=('Franklin Gothic Medium', 40), justify='center')
        self.t_heading.configure(font=('Impact', 100))
    
    
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
        keyboard.on_press(self.keyboardPress)
        self.root = root
        self.data = Database(root)
        self.board = Board(root, self.data)

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

        elif event.name == 'q':
            root.destroy()
        
        self.win_scenario(False)
            
    def win_scenario(self, override):
        lst = [root.getvar(str(num)) for num in self.data.data]
        if self.data.board_answer == lst:
            print('you win!')
            self.board.win_dialog()
            
        if override == True:
            self.board.win_dialog()
        
# Game window properties
root = Tk()
root.title('Sudoku Game')

# Geometry window
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry(f'{window_width}x{window_height}+0+0')
game = Game(root)

# Icon in window
if  platform.system() == 'Linux':
    root.iconphoto(True,  PhotoImage('Icons/icon.png'))
    game.board.main_menu.t_heading.configure(font='Arial Black')
    
else:
    root.iconbitmap('Icons/icon.ico')
    
root.mainloop()