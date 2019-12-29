############################################################################################################
# NAME: BINAIRO SOLVER
# AUTHOR: Christophe Van den Eynde
# FUNCTION: solves Binairo-type puzzles
# USAGE python binairo_solver.py
############################################################################################################

# FUNCTIONS ================================================================================================
# Checking inputted rows for errors ------------------------------------------------------------------------
def InputCheck(row):
    errors = []
    # Row lenght ------------------------------------------------------------------------------------------
    if len(row) != board_size:
        if len(row) < board_size:
            errors.append("[ERROR] Row is to short, a row must contain {} characters".format(board_size))
        else:
            errors.append("[ERROR] Row is to long, a row must contain {} characters".format(board_size))
    # To many of the same number next to each other --------------------------------------------------------
    if "000" in row or "111" in row:
        errors.append("[ERROR] To many instances of the same character (0 or 1) next to eachoter, only 2 instances of 0 or 1 are allowed next to eachoter.")
    # Unwanted characters ------------------------------------ ---------------------------------------------
    for j in row:
        if j not in ["0", "1", "."]:
            errors.append('[ERROR] Unallowed charaters found, only "0", "1" and "." are allowed')
            break
    # To many instances of same number ---------------------------------------------------------------------
    for j in range(0, 2):
        count = str(row).count("{}".format(j))
        if count > (board_size / 2):
            errors.append("[ERROR] Row can only contain {} instances of '{}': found {} instances of '{}'".format(int(board_size / 2), j, count, j))
            break
    return errors
# ==========================================================================================================

# INPUT ====================================================================================================
# Instructions ---------------------------------------------------------------------------------------------
print(
    "\nINSTRUCTIONS:"
    "\n  - Please input the board (row by row) below"
    "\n  - Use a dot for an empty space"
    "\n  - Don't type separators between numbers"
    "\nExample: 1101...001\n"
)

# Board size -----------------------------------------------------------------------------------------------
board_size = input("Size of the board (needs to be an even number): ")
while not board_size.isdigit() or int(board_size) % 2 != 0:
    if board_size.isdigit():
        if int(board_size) % 2 != 0:
            print("[ERROR] board size must be an even number")
    else:
        print("[ERROR] Non-numeric characters found. Board size must be an even number")
    board_size = input("Size of the board (needs to be an even number): ")
board_size = int(board_size)

# Input rows ----------------------------------------------------------------------------------------------
for i in range(1, board_size + 1):
    row = input("Row {}: ".format(i))
    # Catching input errors -------------------------------------------------------------------------------
    while InputCheck(row):
        for error in InputCheck(row):
            print(error)
        row = input("Row {}: ".format(i))
    # SAVE INPUT INTO BOARD -------------------------------------------------------------------------------
    board = []
    board.append(row)
# =========================================================================================================
"""
board_size = 12
board = [
    [".", ".", ".", "1", ".", "0", ".", ".", ".", ".", ".", "."],
    [".", "1", ".", ".", ".", "1", ".", ".", ".", ".", "1", "."],
    [".", ".", ".", ".", ".", "1", ".", "1", ".", ".", ".", "."],
    ["0", ".", ".", ".", ".", ".", ".", ".", ".", ".", "1", "1"],
    [".", ".", ".", ".", "1", ".", ".", ".", "0", ".", ".", "1"],
    [".", ".", ".", "1", ".", ".", ".", ".", "0", ".", "0", "."],
    [".", "1", ".", ".", ".", ".", "0", ".", ".", ".", "0", "."],
    ["0", ".", ".", "0", "0", ".", ".", ".", ".", ".", ".", "."],
    [".", "0", ".", "0", ".", ".", ".", ".", ".", ".", ".", "0"],
    [".", ".", ".", ".", ".", ".", ".", ".", "0", "0", ".", "0"],
    [".", ".", ".", ".", ".", "0", ".", "1", ".", ".", ".", "."],
    ["1", ".", ".", "1", "1", ".", ".", ".", "0", ".", "0", "0"],
]

# FUNCTIONS ============================================================================================

# Checking inputted rows for errors --------------------------------------------------------------------
def InputCheck(row):
    errors = []
    # line lenght --------------------------------------------------------------------------------------
    if len(line) != board_size:
        if len(line) < board_size:
            errors.append("[ERROR] Line is to short, a line must contain {} characters".format(board_size))
        else:
            errors.append("[ERROR] Line is to long, a line must contain {} characters".format(board_size))
    # To many of the same number next to each other ----------------------------------------------------
    if "000" in line or "111" in line:
        errors.append("[ERROR] To many instances of the same character (0 or 1) next to eachoter, only 2 instances of 0 or 1 are allowed next to eachoter.")
    # Unwanted characters ------------------------------------ -----------------------------------------
    for j in line:
        if j not in ["0", "1", "."]:
            errors.append('[ERROR] Unallowed charaters found, only "0", "1" and "." are allowed')
            break
    # CHECK IF LINE CONTAINS TO MANY INSTANCES OF A CERTAIN NUMBER ---------------------------------
    for j in range(0, 2):
        count = str(line).count("{}".format(j))
        if count > (board_size / 2):
            errors.append("[ERROR] Line can only contain {} instances of '{}': found {} instances of '{}'".format(int(board_size / 2), j, count, j))
            break
    return errors


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


# VALIDATION OF POSSIBLE VALUES------------------------------------------------------------------------------
def valid(board, board_size, empty_pos, proposed_val):
    # AVOID TRIPLE (FRONT) - row: .00 --> 100 or .11 --> 011
    if empty_pos[1] >= 0 and empty_pos[1] < (board_size - 2):
        if (
            board[empty_pos[0]][empty_pos[1] + 1] != proposed_val
            and board[empty_pos[0]][empty_pos[1] + 1] != "."
        ) and (
            board[empty_pos[0]][empty_pos[1] + 2] != proposed_val
            and board[empty_pos[0]][empty_pos[1] + 2] != "."
        ):
            if check_max_instances(board, board_size, empty_pos, proposed_val):
                if check_identical(board, board_size, empty_pos, proposed_val):
                    return True
    # AVOID TRIPLE (FRONT) - column: .00 --> 100 or .11 --> 011
    if empty_pos[0] >= 0 and empty_pos[0] < (board_size - 2):
        if (
            board[empty_pos[0] + 1][empty_pos[1]] != proposed_val
            and board[empty_pos[0] + 1][empty_pos[1]] != "."
        ) and (
            board[empty_pos[0] + 2][empty_pos[1]] != proposed_val
            and board[empty_pos[0] + 2][empty_pos[1]] != "."
        ):
            if check_max_instances(board, board_size, empty_pos, proposed_val):
                if check_identical(board, board_size, empty_pos, proposed_val):
                    return True
                return True
    # AVOID TRIPLE (BACK) - row: 00. --> 001 or 11. --> 110
    if empty_pos[1] > 1 and empty_pos[1] <= (board_size - 1):
        if (
            board[empty_pos[0]][empty_pos[1] - 1] != proposed_val
            and board[empty_pos[0]][empty_pos[1] - 1] != "."
        ) and (
            board[empty_pos[0]][empty_pos[1] - 2] != proposed_val
            and board[empty_pos[0]][empty_pos[1] - 2] != "."
        ):
            if check_max_instances(board, board_size, empty_pos, proposed_val):
                if check_identical(board, board_size, empty_pos, proposed_val):
                    return True
    # AVOID TRIPLE (BACK) - col: 00. --> 001 or 11. --> 110
    if empty_pos[0] > 1 and empty_pos[0] <= (board_size - 1):
        if (
            board[empty_pos[0] - 1][empty_pos[1]] != proposed_val
            and board[empty_pos[0] - 1][empty_pos[1]] != "."
        ) and (
            board[empty_pos[0] - 2][empty_pos[1]] != proposed_val
            and board[empty_pos[0] - 2][empty_pos[1]] != "."
        ):
            if check_max_instances(board, board_size, empty_pos, proposed_val):
                if check_identical(board, board_size, empty_pos, proposed_val):
                    return True
    # AVOID TRIPLE (MIDDLE) - row: 0.0 --> 010 or 1.1 --> 101
    if empty_pos[1] > 0 and empty_pos[1] < (board_size - 1):
        if (
            board[empty_pos[0]][empty_pos[1] - 1] != proposed_val
            and board[empty_pos[0]][empty_pos[1] - 1] != "."
        ) and (
            board[empty_pos[0]][empty_pos[1] + 1] != proposed_val
            and board[empty_pos[0]][empty_pos[1] + 1] != "."
        ):
            if check_max_instances(board, board_size, empty_pos, proposed_val):
                if check_identical(board, board_size, empty_pos, proposed_val):
                    return True
    # AVOID TRIPLE (MIDDLE) - column: 0.0 --> 010 or 1.1 --> 101
    if empty_pos[0] > 0 and empty_pos[0] < (board_size - 1):
        if (
            board[empty_pos[0] - 1][empty_pos[1]] != proposed_val
            and board[empty_pos[0] - 1][empty_pos[1]] != "."
        ) and (
            board[empty_pos[0] + 1][empty_pos[1]] != proposed_val
            and board[empty_pos[0] + 1][empty_pos[1]] != "."
        ):
            if check_max_instances(board, board_size, empty_pos, proposed_val):
                if check_identical(board, board_size, empty_pos, proposed_val):
                    return True
    # FILL EMPTY POSITIONS IN ROW/ COLUMN WITH "1" IF ALL ALL "0" ARE FOUND IN THAT ROW/ COLUMN
    if (
        board[empty_pos[0]].count("0") == board_size / 2
        or column(board, empty_pos[1]).count("0") == board_size / 2
        and proposed_val != "0"
    ):
        if check_max_instances(board, board_size, empty_pos, proposed_val):
            if check_identical(board, board_size, empty_pos, proposed_val):
                return True
    # FILL EMPTY POSITIONS IN ROW/ COLUMN WITH "0" IF ALL ALL "1"" ARE FOUND IN THAT ROW/ COLUMN
    if (
        board[empty_pos[0]].count("0") == board_size / 2
        or column(board, empty_pos[1]).count("0") == board_size / 2
        and proposed_val != "1"
    ):
        if check_max_instances(board, board_size, empty_pos, proposed_val):
            if check_identical(board, board_size, empty_pos, proposed_val):
                return True
    return False


# VALIDATION OF POSSIBLE VALUES: MAX INSTANCES OF 1 AND 2 PER ROW CHECK--------------------------------------
def check_max_instances(board, board_size, empty_pos, proposed_val):
    # AVOID MORE INSTANCES OF SAME VALUE THAN ALLOW IN ROW
    if board[empty_pos[0]].count(proposed_val) + 1 > (board_size / 2):
        return False
    # AVOID MORE INSTANCES OF SAME VALUE THAN ALLOW IN COLUMN
    if column(board, empty_pos[1]).count(proposed_val) + 1 > (board_size / 2):
        return False
    return True


# VALIDATION OF POSSIBLE VALUES: CHEK IF PROPOSED VALUE CREATES IDENTICAL ROW/ COLUMNS -----------------------
def check_identical(board, board_size, empty_pos, propposed_val):
    # insert the proposed value into the (test)-board to test if this creates duplicate rows/ columns
    board[empty_pos[0]][empty_pos[1]] == propposed_val
    # create list of columns
    columns = []
    for i in range(0, board_size):
        columns.append(column(board, i))
    # check for identical rows and columns
    for i in range(0, board_size):
        # check if proposed value creates a identical row
        if (
            board[empty_pos[0]] == board[i]
            and empty_pos[0] != i
            # no empty values allowed
            and (not "." in board[empty_pos[0]] and not "." in board[i])
        ):
            return False
        # check if poposed value creates an identical column
        if (
            columns[empty_pos[1]] == columns[i]
            and empty_pos[1] != i
            # no empty values allowed
            and (not "." in columns[empty_pos[1]] and not "." in columns[i])
        ):
            return False
    return True


# CHECK BOARD FOR ERRORS -------------------------------------------------------------------------------
def final_board_check(board, board_size):
    errors = []
    columns = []
    for i in range(0, board_size):
        # [PREPARATION] convert row list to string for easy search
        row = ""
        for j in board[i]:
            row += j
        # [PREPARATION] convert col list to string for easy search
        col = ""
        for j in column(board, i):
            col += j
        # [ERROR CHECK]check row and column for triple values
        if ("000" or "111") in (row or col):
            errors.append(
                "[ERROR] To many instances of the same character (0 or 1) next to eachoter."
            )
        # [ERROR CHECK] if to many 1
        if (row.count("0") or row.count("1")) > board_size / 2:
            errors.append(
                "[ERROR] To many instances of the same character (0 or 1) found in the same row."
            )
        # [ERROR CHECK] if to many 0
        if (col.count("0") or col.count("1")) > board_size / 2:
            errors.append(
                "[ERROR] To many instances of the same character (0 or 1) found in the same column."
            )
        # [ERROR CHECK] if 2 row are same
        for row in board:
            if row == board[i] and board.index(row) != i:
                errors.append("[ERROR] Identical rows found")
                break
        # [ERROR CHECK] if 2 col are same
        columns.append(column(board, i))
        for col in columns:
            if col == columns[i] and columns.index(col) != i:
                errors.append("[ERROR] Identical columns found")
                break
    return errors


# BRUTE FORCE (RECURSIVE) ------------------------------------------------------------------------------
# def brute_force(board):
#     # FIND EMPTY POSITIONS ON BOARD --------------------------------------------------------------------
#     all_empty = find_empty(board)
#     if not all_empty:
#         # solution found
#         return True
#     else:
#         empty_pos = all_empty[0]

#     # CHECK POSSIBLE VALUES FOR EMPTY POSITION & UPDATE BOARD IF FOUND ---------------------------------
#     for value in range(0, 2):
#         # search row, column and box
#         if (
#             # triple prevention
#             # detecting if added value doesnt exceed maximum ammount of instances of this value in teh row/ column
#             # identical row/ column prevention (only if a row is complete)
#         ):
#             # update board if value is valid
#             board[empty_pos[0]][empty_pos[1]] = value
#             # try a value in the next empty position if a valid value was inserted, return true if value is possible
#             if brute_force(board):
#                 return True
#             # reset value if next empty has no valid number
#             board[empty_pos[0]][empty_pos[1]] = "."
#     # required for recursive, says that next empty has no valid number
#     return False


# ======================================================================================================

# SOLVE ================================================================================================
# PRINT ORIGINAL BOARD ---------------------------------------------------------------------------------
print("Original:")
print_board(board)
print()

# CHECK FOR VALID VALUES & UPDATE BOARD IF FOUND -------------------------------------------------------
while len(find_empty(board)) != 0:
    total_empty = len(find_empty(board))
    # SEARCH FOR CERTAIN VALUES AND UPDATE BOARD IF FOUND ----------------------------------------------
    # TRIPLE VALUES
    for empty_pos in find_empty(board):
        # print(empty_pos)
        for i in range(0, 2):
            if valid(board, board_size, empty_pos, str(i)) == True:
                board[empty_pos[0]][empty_pos[1]] = str(i)
                break
        print_board(board)
        print()
    # # COMPLETE ROW/ COLUMN
    # for solution in complete(board, board_size):
    #     board[solution[0][0]][solution[0][1]] = solution[1]
    # BREAK LOOP IF NO MORE VALID VALUES (NO BOARD UPDATES) --------------------------------------------
    if total_empty == len(find_empty(board)):
        break


# CHECK FOR ERRORS IN FINAL BOARD
# errors = check(board, board_size)
# if len(errors) == 0:
#     print("new board")
#     print_board(board)
# else:
#     print("unsolvable:")
#     for error in errors:
#         print(error)


print("\nnew board")
print_board(board)
"""