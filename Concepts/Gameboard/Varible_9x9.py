import tkinter


def create_rcs():
    # Creates list where varibles will be stored
    # rcs stands for rows, collums, square
    for index in range(1, 10):
        gameboard["Rows"]["r{}".format(index)] = []
        gameboard["Collums"]["c{}".format(index)] = []

    for index in range(1, 10):
        gameboard["Square"]["s{}".format(index)] = []


gameboard = {"Start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
             "Rows": {},
             "Collums": {},
             "Square": {},
             "Entire": ["--Undefined--"]}

"""
Help with how to point to each list
print(gameboard["Square"]["s1"])
print(gameboard["Entire"])
"""

create_rcs()
print(gameboard)
