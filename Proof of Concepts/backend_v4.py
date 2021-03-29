from tkinter import *
from tkinter.ttk import Style, Button
import random


def create_rcs():
    # Creates list where varibles will be stored
    # rcs stands for row, column, square
    for i in range(1, 10):
        gb["row"][f"r{i}"] = []
        gb["column"][f"c{i}"] = []
        gb["square"][f"s{i}"] = []


def varible_row():
    row = 1
    for i in range(1, 82):
        gb["row"][f"r{row}"].append(StringVar(root, name=f"{i}"))

        if i % 9 == 0:
            row += 1


def varible_column():
    column = 1
    for i in range(1, 82):
        if column == 10:
            column = 1

        gb["column"][f"c{column}"].append(StringVar(root, name=f"{i}"))
        column += 1


def varible_square():
    # TODO analyze for future improvement
    square = 1
    inside = 1
    endless = 1
    rerun = 0

    for i in range(1, 82):
        gb["square"][f"s{square}"].append(StringVar(root, name=f"{i}"))

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

        elif inside == 3:
            square += 1
            inside = 0

        inside += 1
        endless += 1


def gen():
    # Generates first row
    random.shuffle(gb["start"])
    for i in range(0, 9):
        var = gb["start"][i]
        root.setvar(name=f"{i+1}", value=f"{var}")

    compare = []
    for item in gb["start"]:
        compare.append(str(item))

    name = 10
    index = 0
    loop = True
    while loop:
        temp_r = []
        temp_c = []
        temp_s = []

        # TODO Improve here in the loop where everthing is the same
        # TODO Make a range 3 loop and just toggle between r,c,s
        for c in ["r", "c", "s"]:
            if c == "r":
                db = "row"
            elif c == "c":
                db = "column"
            elif c == "s":
                db = "square"

            for i in range(1, 10):
                for z in gb[f"{db}"][f"{c}{i}"]:
                    if str(name) == str(z):
                        for x in range(0, 9):

                            # TODO make all of this into one
                            if c == "r":
                                if gb["row"][f"r{i}"][x].get() in compare:
                                    temp_r.append(int(gb["row"][f"r{i}"][x].get()))
                                else:
                                    temp_r.append(gb["row"][f"r{i}"][x].get())

                            elif c == "c":
                                if gb["column"][f"c{i}"][x].get() in compare:
                                    temp_c.append(int(gb["column"][f"c{i}"][x].get()))
                                else:
                                    temp_c.append(gb["column"][f"c{i}"][x].get())

                            elif c == "s":
                                if gb["square"][f"s{i}"][x].get() in compare:
                                    temp_s.append(int(gb["square"][f"s{i}"][x].get()))

                                else:
                                    temp_s.append(gb["square"][f"s{i}"][x].get())

        random.shuffle(gb["start"])
        for count, num in enumerate(gb["start"]):
            check = True
            if num in temp_r or num in temp_c or num in temp_s:
                check = False

            if check == True:
                root.setvar(name=f"{name}", value=f"{num}")

                # ? Replace index var...?
                name += 1
                index += 1
                if index == 9:
                    index = 0
                break

            if (count + 1) == 9:
                name = name - index
                index = 0

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
gb = {
    "start": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "row": {},
    "column": {},
    "square": {},
    "entire": ["--Undefined--"],
}

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

# Generates board
gen()
print("done!")

# Makes gameboard with varibels
gameboard()

root.mainloop()
