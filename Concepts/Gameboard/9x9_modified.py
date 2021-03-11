from tkinter import Tk
from tkinter.ttk import Style, Button
import random

root = Tk()
root.title("9x9")
root.geometry("400x350")

# Style on lable
style = Style()
style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

# List of labels
first_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(first_row)

rows = [[], [], [], [], [], [], [], [], []]
for index in range(9):
    if index == 0:
        for number in first_row:
            rows[index].append(Button(root, text=number, style="TButton"))
    else:
        for _ in range(9):
            rows[index].append(Button(root, text="-", style="TButton"))

# Visualize all of them
for count, button in enumerate(rows):
    for index in range(9):
        button[index].grid(row=count, column=index)

"""
# Change the first one of all
button = rows[0][0]
button.configure(text="2")
button.update()
"""

# Print out the program
root.mainloop()
