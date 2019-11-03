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

board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9]
         ]

# PRINT THE BOARD ======================================================================================


def print_board(board):
    # CYCLE TROUGH ROWS --------------------------------------------------------------------------------
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- "*12)
    # CYCLE THROUGH COLUMNS ----------------------------------------------------------------------------
        for j in range(len(board[i])):  # column
            if j % 3 == 0 and j != 0:
                print(" |", end='')
            print(" {}".format(board[i][j]), end='')
            if j == 8:
                print()
# ======================================================================================================


print_board(board)
