from tkinter import *
from typing import List

root = Tk()

# intvar = IntVar(root, value=25, name="2")
# print(intvar.get())

lst = [1, 2, 3, 4, 5, 6]

IntVar(root, name="int")
root.setvar(name="int", value=8)

value = root.getvar("int")

if value in lst:
    print("True")
else:
    print("False")


def getSquareFor(index):
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

    # * Gets wich square
    return lst[((column // 3) + (row // 3 * 3))]


print(getSquareFor(80))
