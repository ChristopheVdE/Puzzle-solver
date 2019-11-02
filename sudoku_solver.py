# SUDOKU SOLVER

# INPUT THE BOARD ======================================================================================
board = []
for i in range(1, 10):
    line = input("Line {}: ".format(i))
    # CHECK IF INPUT MEETS REQUIREMENTS-----------------------------------------------------------------
    while not len(line) == 9 or not line.isdigit():
        if len(line) < 9:
            print("[ERROR] Line is to short, a line must contain 9 numbers")
        if len(line) > 9:
            print("[ERROR] Line is to long, a line must contain 9 numbers")
        if not line.isdigit():
            print("[ERROR] Line can only contain numbers")
        line = input("Line {}: ".format(i))
    # SAVE INPUT INTO BOARD ----------------------------------------------------------------------------
    row = []
    for num in line:
        row.append(num)
    board.append(row)
print(board)
# ======================================================================================================
