from tkinter import *
from tkinter.ttk import Style, Button
import random


def create_rcs():
    # Creates list where varibles will be stored
    # rcs stands for row, column, square
    for i in range(1, 10):
        gb["row"]["r{}".format(i)] = []
        gb["column"]["c{}".format(i)] = []

    for i in range(1, 10):
        gb["square"]["s{}".format(i)] = []


def varible_row():
    row = 1
    for i in range(1, 82):
        gb["row"]["r{}".format(row)].append(
            StringVar(root, name="{}".format(i)))

        if i % 9 == 0:
            row += 1


def varible_column():
    column = 1
    for i in range(1, 82):
        if column == 10:
            column = 1

        gb["column"]["c{}".format(column)].append(
            StringVar(root, name="{}".format(i)))
        column += 1


def varible_square():
    square = 1
    inside = 1
    endless = 1
    rerun = 0

    for i in range(1, 82):
        gb["square"]["s{}".format(square)].append(
            StringVar(root, name="{}".format(i)))

        if rerun == 2 and endless == 9:
            rerun = 0
            inside = 0
            endless = 0
            square += 1

        elif endless == 9:
            square -= 2
            inside = 0
            endless = 0
            rerun += 1

        # * Works
        elif inside == 3:
            square += 1
            inside = 0

        inside += 1
        endless += 1


def gen():
    # Generates first row
    random.shuffle(gb["start"])
    for i in range(0, 9):
        root.setvar(name="{}".format(i+1), value="{}".format(gb["start"][i]))

    # Generates the rest
    name = 10
    lst = []
    temp_r = []
    temp_c = []
    temp_s = []
    for index in range(2, 10):
        for i in range(3):
            if i == 0:
                key = "r"
                db = "row"
                temp_r = lst

            if i == 1:
                key = "c"
                db = "column"
                temp_c = lst

            if i == 2:
                key = "s"
                db = "square"
                temp_s = lst

            #! Not working
            #print("db", db)
            #print("key", key)
            for find in gb["{}".format(db)]["{}{}".format(key, index)]:
                if str(name) == str(find):
                    for x in range(0, 9):
                        if gb["{}".format(db)]["{}{}".format(key, index)][x].get() in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            lst.append(
                                int(gb["{}".format(db)]["{}{}".format(key, index)][x].get()))

                        else:
                            lst.append(gb["{}".format(db)]
                                       ["{}{}".format(key, index)][x].get())

                    random.shuffle(gb["start"])
                    for num in gb["start"]:
                        row = True
                        coll = True
                        sqr = True

                        print(num)
                        print(temp_r)
                        print(temp_c)
                        print(temp_s)
                        if num in temp_r:
                            row = False

                        if num in temp_c:
                            coll = False

                        if num in temp_s:
                            sqr = False

                        if row == True and coll == True and sqr == True:
                            root.setvar(name="{}".format(name),
                                        value="{}".format(num))

                            temp_r = []
                            temp_c = []
                            temp_s = []
                            name += 1

        # print(temp_r)
        # print(temp_c)
        # print(temp_s)
        # input("")


def gameboard():
    row = 0
    column = 0
    for i in range(1, 82):
        button = Button(root, text=root.getvar(
            "{}".format(i)), style="TButton")
        button.grid(row=row, column=column)

        column += 1
        if i % 9 == 0:
            column = 0
            row += 1


# Data base
gb = {"start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
      "row": {},
      "column": {},
      "square": {},
      "entire": ["--Undefined--"]}

# Make tkinter
root = Tk()
root.title("9x9")
root.geometry("450x350")

# Style
style = Style()
style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

# Create data base function
create_rcs()

# Create varibles function
varible_row()
varible_column()
varible_square()

# Generate the entire board
"""
dawda = 0
while True:
    temp = []
    gen()
    for i in range(1, 82):
        var = root.getvar(name="{}".format(i))
        if var == "":
            continue

        else:
            temp.append(var)

    if len(temp) == 81:
        break
    temp = []

    if dawda % 1000 == 0:
        print(dawda)
    dawda += 1
"""
gen()

# Makes gameboard with varibels
gameboard()

root.mainloop()
