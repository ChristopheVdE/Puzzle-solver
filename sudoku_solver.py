# SUDOKU SOLVER

# # INPUT THE BOARD ======================================================================================
# board = []
# for i in range(1, 10):
#     line = input("Line {}: ".format(i))
#     # CHECK IF INPUT MEETS REQUIREMENTS-----------------------------------------------------------------
#     while not len(line) == 9 or not line.isdigit():
#         if len(line) < 9:
#             print("[ERROR] Line is to short, a line must contain 9 numbers")
#         if len(line) > 9:
#             print("[ERROR] Line is to long, a line must contain 9 numbers")
#         if not line.isdigit():
#             print("[ERROR] Line can only contain numbers")
#         line = input("Line {}: ".format(i))
#     # SAVE INPUT INTO BOARD ----------------------------------------------------------------------------
#     row = []
#     for num in line:
#         row.append(num)
#     board.append(row)
# # ======================================================================================================

# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7],
# ]

# Hardest sudoku ever
board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

# FUNCTIONS ============================================================================================
# PRINT SUDOKU BOARD -----------------------------------------------------------------------------------
def print_sudoku(board):
    # CYCLE TROUGH ROWS --------------------------------------------------------------------------------
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 12)
        # CYCLE THROUGH COLUMNS ------------------------------------------------------------------------
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" |", end="")
            print(" {}".format(board[i][j]), end="")
            if j == (len(board) - 1):
                print()


# FIND EMPTY VALUES ------------------------------------------------------------------------------------
def find_empty(board):
    empty_values = []
    for i in range(len(board)):  # row
        for j in range(len(board[i])):  # column
            if board[i][j] == 0:
                empty_values.append((i, j))
    return empty_values


# FIND VALUES FROM COlUMN ------------------------------------------------------------------------------
def column(board, col):
    column_values = []
    for row in board:
        column_values.append(row[col])
    return column_values


# FIND VALUES FROM BOX ---------------------------------------------------------------------------------
def box(board, empty_pos):
    # search 3x3 box
    box_x = empty_pos[0] // 3
    box_y = empty_pos[1] // 3
    # make list of values in box
    box_values = []
    for j in range(box_x * 3, box_x * 3 + 3):
        for k in range(box_y * 3, box_y * 3 + 3):
            box_values.append(board[j][k])
    return box_values


# TEST FOR CERTAIN VALUES ------------------------------------------------------------------------------
def certain(board, empty_pos):
    test = []
    # check for possible values (1-9)
    for value in range(1, 10):
        # search row, column and box
        if (
            not value in board[empty_pos[0]]  # rox
            and not value in column(board, empty_pos[1])  # column
            and not value in box(board, empty_pos)  # box
        ):
            test.append((value, True))
    return test


# BRUTE FORCE (RECURSIVE) ------------------------------------------------------------------------------
def brute_force(board):
    # FIND EMPTY POSITIONS ON BOARD --------------------------------------------------------------------
    empty_pos = find_empty(board)
    if not empty_pos:
        # solution found
        return True
    else:
        empty_pos = empty_pos[0]

    # CHECK POSSIBLE VALUES FOR EMPTY POSITION & UPDATE BOARD IF FOUND ---------------------------------
    for value in range(1, 10):
        # search row, column and box
        if (
            not value in board[empty_pos[0]]  # rox
            and not value in column(board, empty_pos[1])  # column
            and not value in box(board, empty_pos)  # box
        ):
            # update board if value is valid
            board[empty_pos[0]][empty_pos[1]] = value
            # try a value in the next empty position if a valid value was inserted
            if brute_force(board):
                return True
            board[empty_pos[0]][empty_pos[1]] = 0
    return False


# ======================================================================================================


# SOLVE ================================================================================================
# PRINT ORIGINAL BOARD ---------------------------------------------------------------------------------
print_sudoku(board)

# CHECK FOR CERTAIN VALUES & UPDATE BOARD IF FOUND -----------------------------------------------------
while len(find_empty(board)) != 0:
    og_board = board
    # SEARCH FOR CERTAIN VALUES AND UPDATE BOARD IF FOUND ----------------------------------------------
    for empty_pos in find_empty(board):
        # print("row = {}".format(board[empty_pos[0]]))
        # print("col = {}".format(column(board, empty_pos[1])))
        # print("box = {}".format(box(board, empty_pos)))
        # print(empty_pos, certain(board, empty_pos))
        if len(certain(board, empty_pos)) == 1:
            board[empty_pos[0]][empty_pos[1]] = certain(board, empty_pos)[0][0]
    # BREAK LOOP IF NO MORE CERTAIN VALUES (NO BOARD UPDATES) ------------------------------------------
    if og_board == board:
        break

# USE BRUTE FORCE IF THERE ARE STILL EMPTY VALUES AND THERE ARE NO MORE CERTAIN VALUES -----------------
if (len(find_empty(board)) != 0) and (og_board == board):
    brute_force(board)

# PRINT SOLVED BOARD -----------------------------------------------------------------------------------
print()
print_sudoku(board)

# ======================================================================================================
