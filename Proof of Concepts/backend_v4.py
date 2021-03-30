from tkinter import *
from tkinter.ttk import Style, Button
import random

# TODO make import better, with out using star
# * Imports to many functions that are not needed


def create_database():
    # Creates list where varibles will be stored
    for i in range(1, 10):
        data["row"][f"r{i}"] = []
        data["column"][f"c{i}"] = []
        data["square"][f"s{i}"] = []

    # TODO take a look for further optimization
    row = 1
    column = 1
    square = 1

    for name in range(1, 82):

        data["row"][f"r{row}"].append(StringVar(root, name=f"{name}"))
        data["column"][f"c{column}"].append(StringVar(root, name=f"{name}"))
        data["square"][f"s{square}"].append(StringVar(root, name=f"{name}"))

        if name % 9 == 0:
            row += 1
            column = 0
            square = 1

            if row > 3 and not row > 6:
                square += 3

            if row > 6 and not row > 9:
                square += 6

        # *Square ticks up  here:
        if column == 3 or column == 6:
            square += 1

        column += 1


def gen():
    # Generates first row
    random.shuffle(data["start"])
    for i in range(0, 9):
        var = data["start"][i]
        root.setvar(name=f"{i+1}", value=f"{var}")

    compare = []
    for item in data["start"]:
        compare.append(str(item))

    name = 10
    loop = True
    while loop:
        temp_r = []
        temp_c = []
        temp_s = []

        # TODO Improve here in the loop where everthing is the same
        # TODO Make a range 3 loop and just toggle between r,c,s
        for c in ["r", "c", "s"]:
            if c == "r":
                section = "row"
                lst = temp_r

            elif c == "c":
                section = "column"
                lst = temp_c

            elif c == "s":
                section = "square"
                lst = temp_s

            # ! Does not work to replace f"{c}{i}" to subsection
            # TODO Find solution
            subsection = c + str(i)
            # print(subsection)

            for i in range(1, 10):
                for z in data[f"{section}"][f"{c + str(i)}"]:
                    if str(name) == str(z):
                        for x in range(0, 9):

                            # TODO Make it easier to read
                            # ? Choose better varibale names?
                            if data[f"{section}"][f"{c}{i}"][x].get() in compare:
                                lst.append(int(data[f"{section}"][f"{c}{i}"][x].get()))
                            else:
                                lst.append(data[f"{section}"][f"{c}{i}"][x].get())

        random.shuffle(data["start"])
        for count, num in enumerate(data["start"]):
            check = True
            if num in temp_r or num in temp_c or num in temp_s:
                check = False

            if check == True:
                root.setvar(name=f"{name}", value=f"{num}")
                name += 1
                break

            if (count + 1) == 9:
                name = name - (count - 1)

                for i in range(9):
                    root.setvar(name=f"{name+i}", value="")
                break

        if name == 82:
            loop = False


def gameboard():
    row = 0
    column = 0
    for i in range(1, 82):
        button = Button(root, text=root.getvar(f"{i}"), style="TButton")
        button.grid(row=row, column=column)

        column += 1
        if i % 9 == 0:
            column = 0
            row += 1


# Data base
data = {
    "row": {},
    "column": {},
    "square": {},
    "entire": ["--Undefined--"],
    "start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
}

# Make tkinter
root = Tk()
root.title("9x9")
root.geometry("450x350")

# Style
style = Style()
style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

# Create data base
create_database()

# Generates board
gen()
print("done!")

# Makes gameboard with varibels
gameboard()

root.mainloop()
