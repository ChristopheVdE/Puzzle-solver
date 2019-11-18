# SUDOKU SOLVER

# INPUT THE BOARD ======================================================================================
print(
    "\nINSTRUCTIONS:"
    "\n  - Please input the board (row by row) below"
    "\n  - Use a dot for an empty space"
    "\n  - Don't type separators between numbers"
    "\n  Example: 1101...001\n"
)
# SET BOARD SIZE ---------------------------------------------------------------------------------------
board = []
board_size = input("Size of the board (needs to be an even number): ")
while not board_size.isdigit() or int(board_size) % 2 != 0:
    if board_size.isdigit():
        if int(board_size) % 2 != 0:
            print("[ERROR] board size must be an even number")
    else:
        print("[ERROR] Non-numeric characters found. Board size must be an even number")
    board_size = input("Size of the board (needs to be an even number): ")
board_size = int(board_size)

# INPUT ROWS -------------------------------------------------------------------------------------------
for i in range(1, board_size + 1):
    line = input("Line {}: ".format(i))
    # ERROR CHECKS -------------------------------------------------------------------------------------
    while True:
        errors = []
        # CHECK IF INPUT MEETS REQUIRERED LENGHT -------------------------------------------------------
        if len(line) != board_size:
            if len(line) < board_size:
                errors.append(
                    "[ERROR] Line is to short, a line must contain {} characters".format(
                        board_size
                    )
                )
            else:
                errors.append(
                    "[ERROR] Line is to long, a line must contain {} characters".format(
                        board_size
                    )
                )
        # CHECK IF LINE CONTAINS UNWANTED CHARACTERS (lETTERS) -----------------------------------------
        for j in line:
            if j != "0" and j != "1" and j != ".":
                errors.append(
                    '[ERROR] Unallowed charaters found, only "0", "1" and "." are allowed'
                )
                break
        # CHECK IF LINE CONTAINS TO MANY INSTANCES OF A CERTAIN NUMBER ---------------------------------
        for j in range(0, 2):
            count = str(line).count("{}".format(j))
            if count > (board_size / 2):
                errors.append(
                    "[ERROR] Line can only contain {} instances of '{}': found {} instances of '{}'".format(
                        int(board_size / 2), j, count, j
                    )
                )
                break
        # ERROR PRINTING -------------------------------------------------------------------------------
        # NO ERRORS --> SKIP TO INPUT NEXT LINE
        if len(errors) == 0:
            break
        # ERRORS FOUND --> PRINT ERRORS AND RE-INPUT CURRENT LINE
        else:
            for error in errors:
                print(error)
            line = input("Line {}: ".format(i))
    # SAVE INPUT INTO BOARD ----------------------------------------------------------------------------
    row = []
    for num in line:
        row.append(num)
    board.append(row)
# ======================================================================================================

# CERTAIN VALUES

# for row in rows:
#     if 0,0 in row:
#     if 1,1 in row:
#     if 0, ,0 in row:
#     if 1, ,1 in row:

# for col in columns:
