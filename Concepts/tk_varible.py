# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
root = Tk()

# Tkinter variables
# initialization using constructor
intvar = IntVar(root, value=25, name="2")
strvar = StringVar(root, name="string", value="Hello!")
boolvar = BooleanVar(root, True)
doublevar = DoubleVar(root, 10.25)

print(strvar.get())
root.setvar(name="string", value="Test...")
print(strvar.get())
