from tkinter import *

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
