from tkinter import *


def create_rcs():
    # Creates list where varibles will be stored
    # rcs stands for rows, Collumn, square
    for i in range(1, 10):
        gb["rows"]["r{}".format(i)] = []
        gb["collumn"]["c{}".format(i)] = []

    for i in range(1, 10):
        gb["square"]["s{}".format(i)] = []


def varible_row():
    row = 1
    for i in range(1, 82):
        gb["rows"]["r{}".format(row)].append(
            StringVar(root, name="{}".format(i)))

        if i % 9 == 0:
            row += 1


def varible_collumn():
    collumn = 1
    for i in range(1, 82):
        if collumn == 10:
            collumn = 1

        gb["collumn"]["c{}".format(collumn)].append(
            StringVar(root, name="{}".format(i)))
        collumn += 1


def varible_square():
    #! not working in square 3
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

    # * Main code
gb = {"start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
      "rows": {},
      "collumn": {},
      "square": {},
      "entire": ["--Undefined--"]}

# Make tkinter
root = Tk()

# Create data base function
create_rcs()

# Create varibles function
varible_row()
varible_collumn()
varible_square()

for i in range(1, 10):
    print(len(gb["square"]["s{}".format(i)]))
