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

# FUNCTIONS ============================================================================================
# BOARD PRINTING ---------------------------------------------------------------------------------------
def print_board(board):
    for i in board:
        print(i)


# FIND EMPTY VALUES ------------------------------------------------------------------------------------
def find_empty(board):
    empty_values = []
    for i in range(len(board)):  # row
        for j in range(len(board[i])):  # column
            if board[i][j] == ".":
                empty_values.append((i, j))
    return empty_values


# CREATE LIST OF ALL VALUES OF A COLUMN ----------------------------------------------------------------
def column(board, col):
    column_values = []
    for row in board:
        column_values.append(row[col])
    return column_values


# ======================================================================================================

# VALID VALUES -----------------------------------------------------------------------------------------
def valid(board, empty_value):
    # empty_value[0] = x =  row
    # empty_value[1] = y =  col
    # CHECK ROW ----------------------------------------------------------------------------------------
    if empty_value[1] >= 0 and empty_value[1] < (len(board) - 2):
        # .00 --> 100
        if (
            board[empty_value[0]][empty_value[1] + 1] == "0"
            and board[empty_value[0]][empty_value[1] + 2] == "0"
        ):
            return "1"
        # .11 --> 011
        elif (
            board[empty_value[0]][empty_value[1] + 1] == "1"
            and board[empty_value[0]][empty_value[1] + 2] == "1"
        ):
            return "0"
    if empty_value[1] > 1 and empty_value[1] <= (len(board) - 1):
        # 00. --> 001
        if (
            board[empty_value[0]][empty_value[1] - 1] == "0"
            and board[empty_value[0]][empty_value[1] - 2] == "0"
        ):
            return "1"
        # 11. --> 110
        elif (
            board[empty_value[0]][empty_value[1] - 1] == "1"
            and board[empty_value[0]][empty_value[1] - 2] == "1"
        ):
            return "0"
        # else:
        #     return "."
    if empty_value[1] > 0 and empty_value[1] < (len(board) - 1):
        # 0.0 --> 010
        if (
            board[empty_value[0]][empty_value[1] - 1] == "0"
            and board[empty_value[0]][empty_value[1] + 1] == "0"
        ):
            return "1"
        # 1.1 --> 101
        elif (
            board[empty_value[0]][empty_value[1] - 1] == "1"
            and board[empty_value[0]][empty_value[1] + 1] == "1"
        ):
            return "0"
    # CHECK COLUMN --------------------------------------------------------------------------------------
    if empty_value[0] >= 0 and empty_value[0] < (len(board) - 2):
        # .00 --> 100
        if (
            board[empty_value[0] + 1][empty_value[1]] == "0"
            and board[empty_value[0] + 2][empty_value[1]] == "0"
        ):
            return "1"
        # .11 --> 011
        elif (
            board[empty_value[0] + 1][empty_value[1]] == "1"
            and board[empty_value[0] + 2][empty_value[1]] == "1"
        ):
            return "0"
    if empty_value[0] > 1 and empty_value[0] <= (len(board) - 1):
        # 00. --> 001
        if (
            board[empty_value[0] - 1][empty_value[1]] == "0"
            and board[empty_value[0] - 2][empty_value[1]] == "0"
        ):
            return "1"
        # 11. --> 110
        elif (
            board[empty_value[0] - 1][empty_value[1]] == "1"
            and board[empty_value[0] - 2][empty_value[1]] == "1"
        ):
            return "0"
        # else:
        #     return "."
    if empty_value[0] > 0 and empty_value[0] < (len(board) - 1):
        # 0.0 --> 010
        if (
            board[empty_value[0] - 1][empty_value[1]] == "0"
            and board[empty_value[0] + 1][empty_value[1]] == "0"
        ):
            return "1"
        # 1.1 --> 101
        elif (
            board[empty_value[0] - 1][empty_value[1]] == "1"
            and board[empty_value[0] + 1][empty_value[1]] == "1"
        ):
            return "0"
        else:
            return "."
    else:
        return "."


# SOLVE ================================================================================================
# PRINT ORIGINAL BOARD ---------------------------------------------------------------------------------
print("Original:")
print_board(board)

# CHECK FOR VALID VALUES & UPDATE BOARD IF FOUND -------------------------------------------------------
while len(find_empty(board)) != 0:
    og_board = board

    # SEARCH FOR VALID VALUES AND UPDATE BOARD IF FOUND ------------------------------------------------
    for empty_pos in find_empty(board):

        # CERTAIN OPTIONS FOUND: UPDATE BOARD ----------------------------------------------------------
        board[empty_pos[0]][empty_pos[1]] = valid(board, empty_pos)
        print(board)

    # BREAK LOOP IF NO MORE VALID VALUES (NO BOARD UPDATES) --------------------------------------------
    if og_board == board:
        break

print("new board")
print_board(board)
