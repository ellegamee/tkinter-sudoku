"""
=============
| Pseudokod |
=============
 1 2 3 4 5 6 7 8 9
 1 X 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9
"""
X = "This is us"
columner = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [X, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
rows = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, X, 0, 0, 0, 0, 0, 0],
]


def getSquareStart(column):
    if column >= 0 and column <= 2:
        return 0
    if column >= 3 and column <= 5:
        return 3
    if column >= 6 and column <= 8:
        return 6


def squareNumbers(number):
    return [
        getSquareStart(number),
        getSquareStart(number) + 1,
        getSquareStart(number) + 2,
    ]


def isSten(test_number, column, row):

    # Column
    kompisColumner = []
    for col in squareNumbers(column):
        if col != column:
            kompisColumner.append(col)

    print("kompisColumner", kompisColumner)

    # Row
    kompisRows = []
    for roww in squareNumbers(row):
        if roww != row:
            kompisRows.append(roww)

    print("kompisRows", kompisRows)

    # Check if this is a sten number
    if (
        test_number not in columner[column]
        and test_number in columner[kompisColumner[0]]
        and test_number in columner[kompisColumner[1]]
        and test_number not in rows[row]
        and test_number in rows[kompisRows[0]]
        and test_number in rows[kompisRows[1]]
    ):
        return True
    return False


print("0", isSten(7, 0, 2))


def isNum100Sure(test_number, column, row1):
    row = 0
    square = 0
    column = column

    if column > 2 and not column > 5:
        square += 1

    if column > 5 and not column > 8:
        square += 2

    if row1 > 2 and not row1 > 5:
        row += 3

    if row1 > 5 and not row1 > 8:
        row += 6

    return [
        "Coll",
        (square * 3),
        (square * 3) + 1,
        (square * 3) + 2,
        "Rows",
        row,
        row + 1,
        row + 2,
    ]

    # squareStartCol = ((int((column / 9) * 3) + 1) * 3) - 3
    # kompisColumn = [
    #    squareStartCol,
    #    squareStartCol + 1,
    #    squareStartCol + 2,
    # ]
    # return kompisColumn


print(isNum100Sure(0, 3, 7))
