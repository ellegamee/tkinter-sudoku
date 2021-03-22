"""
Vesion 1: #!(thinking about it makes me find lots of problems with it)
Inside of rows, collums and square will be tk varibles with names
(r1:1, c1:1, s1:1 etc.) I think this will be a better solution because
then we can do a lot of if number is inside list. The big problem can
come where there are 3 varibles that specify to the same number and
that can start a problem in how we name them. We want all three to
change at the same time.
"""

gameboard = {"Base": [1, 2, 3, 4, 5, 6, 7, 8, 9],
             "Rows": {"r1": [], "r2": [], "r3": []},
             "Collums": {"c1": [], "c2": [], "c3": []},
             "Square": {"s1": [], "s2": [], "s3": []},
             "Entire": ["Entire but not really"]}

# Easy way to point at a number
print(gameboard["Square"]["s1"])
print(gameboard["Entire"])

"""
Version 2: #*(easy good method but will be harder to compare)
Simple list with all tkinter varibles that you can specify with easy indexing,
by height you take minus 9 in a loop until you get to the base value. You stop
when you get to zero. In width you can count wich row you are on and then have
the left most index in mind and count down until that index. Seems more complicated
but could be easier to handle.
"""

"""
Version 3:
This version should be a combination between the second one and the first one with
easy to work with lists and an advanced version with a lot of groups. The problem
with the first version is the naming system wich makes the same button have different
tkinter veribles names that sucks.

Just use names that count up like indexing like the second version. This makes it
easy to specify and works almost like the first one so you can check easy if the value
is inside of the list. Use a temp list to get the values out of every tkvarible and
then make a if statement and check if the value I have right now is in the temp list
or not.

A little advanced but get's the best out of both world!
"""
