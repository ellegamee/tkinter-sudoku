gameboard = {"Base": [1, 2, 3, 4, 5, 6, 7, 8, 9],
             "Rows": {"r1": [], "r2": [], "r3": []},
             "Collums": {"c1": [], "c2": [], "c3": []},
             "Square": {"s1": [], "s2": [], "s3": []},
             "Entire": ["Entire but not really"]}

# Easy way to point at a number
print(gameboard["Square"]["s1"])
print(gameboard["Entire"])
