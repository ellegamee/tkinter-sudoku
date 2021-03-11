from tkinter import Tk
from tkinter.ttk import Style, Button

root = Tk()
root.title("9x9")
root.geometry("400x350")

# Style on lable
style = Style()
style.configure("TButton", font=("calibri", 15, "bold"), height=10, width=3)

# List of labels
rows = [[], [], [], [], [], [], [], [], []]
for index in range(9):
    for number in range(1, 10):
        rows[index].append(Button(root, text=number, style="TButton"))

# Visualize all of them
for count, button in enumerate(rows):
    for index in range(9):
        button[index].grid(row=index, column=count)

"""
# Change the first one of all
button = rows[0][0]
button.configure(text="2")
button.update()
"""

# Print out the program
root.mainloop()
