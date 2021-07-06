from tkinter import *
import tkinter
from tkinter.ttk import Style, Button
from functools import partial
import random

# TODO make import better, with out using star
# * Wildcard problem


def create_database():
    # Creates list where varibles will be stored
    for index in range(9):
        data["row"][f"r{index}"] = []
        data["column"][f"c{index}"] = []
        data["square"][f"s{index}"] = []

    # * Creatas all names
    row = 0
    column = 0
    square = 0

    for name in range(81):
        data["row"][f"r{row}"].append(StringVar(root, name=f"{name}"))
        data["column"][f"c{column}"].append(StringVar(root, name=f"{name}"))
        data["square"][f"s{square}"].append(StringVar(root, name=f"{name}"))

        if (name + 1) % 9 == 0:
            row += 1
            column = -1
            square = 0

            if row > 2 and not row > 5:
                square += 3

            if row > 5 and not row > 8:
                square += 6

        if column == 2 or column == 5:
            square += 1

        column += 1


def number_generator():
    # Generates first row
    """
    random.shuffle(data["start"])
    for i in range(9):
        var = data["start"][i]
        root.setvar(name=f"{i}", value=f"{var}")
    """

    compare = []
    for item in data["start"]:
        compare.append(str(item))

    name = 0
    loop = True
    while loop:
        temp_r = []
        temp_c = []
        temp_s = []

        # TODO Fix better names for list's
        lst_sector = ["row", "column", "square"]
        lst_lst = [temp_r, temp_c, temp_s]
        lst_c = ["r", "c", "s"]
        for sector, lst, c in zip(lst_sector, lst_lst, lst_c):

            for i in range(9):
                subsector = f"{c}{i}"

                for z in data[f"{sector}"][f"{subsector}"]:
                    if str(name) == str(z):
                        for obj in range(9):

                            if data[f"{sector}"][f"{subsector}"][obj].get() in compare:

                                # ! This formating is odd
                                # ? Worth fixing?
                                lst.append(
                                    int(data[f"{sector}"]
                                        [f"{subsector}"][obj].get())
                                )

                            else:
                                lst.append(data[f"{sector}"]
                                           [f"{subsector}"][obj].get())

        print(temp_c)
        print(temp_r)
        print(temp_s)

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

        if name == 81:
            loop = False

    # * Makes copy of entire grid
    for obj in range(81):
        data["entire"].append(root.getvar(f"{obj}"))


def remove_num():

    zero = False
    removed = 0
    while removed <= (81 - 34):
        index = random.randrange(81)
        # print(index)

        # * Check if button is empty
        if root.getvar(f"{index}") == "":
            continue

        temp = []
        for i in range(81):
            temp.append(root.getvar(f"{i}"))
        temp = "".join(temp)

        if temp.count(root.getvar(f"{index}")) == 0 and zero == False:
            root.setvar(f"{index}", value="")

            zero = True
            removed += 1
            continue

        if temp.count(root.getvar(f"{index}")) > 0:
            root.setvar(f"{index}", value="")

            removed += 1
            continue


def change_num(name):
    Button(name=f"{name}")
    root.update()

    data["button"][name]["text"] = input("Inside: ")
    root.setvar(name=f"{name}", value="C")


def gameboard():
    row = 0
    column = 0
    for i in range(81):

        data["button"].append(
            Button(
                root,
                name=f"b{i}",
                style="TButton",
                command=partial(change_num, i),
            )
        )
        data["button"][i].grid(row=row, column=column)

        column += 1
        if (i + 1) % 9 == 0:
            column = 0
            row += 1

    # * Visual beutie
    # ? Can i make these two for into one
    for i in range(81):
        data["button"][i]["text"] = root.getvar(f"{i}")
        root.update()
        root.after(20)


# Data base
data = {
    "row": {},
    "column": {},
    "square": {},
    "entire": [],
    "button": [],
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
number_generator()
print("done!")

# Makes gameboard with varibels
remove_num()
gameboard()
print("live!")

root.mainloop()
