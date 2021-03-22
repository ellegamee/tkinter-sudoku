# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
root = Tk()

# Tkinter variables
# initialization using constructor
intvar = IntVar(root, value=25, name="2")
strvar = StringVar(root, name="string")
boolvar = BooleanVar(root, True)
doublevar = DoubleVar(root, 10.25)

lst = []
lst.append(StringVar(root, name="test", value="hi"))

# Test to see if you can point at index in list
print(lst)
# * Really important
print(lst[0].get())


# * Really important!!!!!
StringVar(root, name="string2")

# * Really important!!!!
root.setvar(name="string2", value="Test2...")
print(root.getvar("string2"))


# ! Not really best solution
print()
root.setvar(name="string", value="Test...")
print(strvar.get())
strvar.set("test2")
print(strvar.get())

# TODO Good method on using the tkvarible on button
bt1 = Button(root, textvariable="string2")
bt1.pack()
root.mainloop()
