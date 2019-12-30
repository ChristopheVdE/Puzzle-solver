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
# Print Board ----------------------------------------------------------------------------------------------

# Transpose board to get columns ---------------------------------------------------------------------------
def TransposeBoard(board):
    columns = []
    for column_nr in range(len(board)):
        line = ''
        for row in board:
            line += row[column_nr]
        columns.append(line)
    return columns

# Find empty -----------------------------------------------------------------------------------------------

def CountEmpty(board):
    empty = 0
    for line in range(len(board)):
        for char in board[line]:
            if char == ".":
                empty += 1
    return empty

# Find certain values --------------------------------------------------------------------------------------
def Certain(board):
    for line in range(len(board)):
        for i in range(0, 2):
            if i == 0:
                if ".00" in board[line]:   return (1, (line, board[line].index(".00")))
                elif "0.0" in board[line]: return (1, (line, board[line].index("0.0") + 1))
                elif "00." in board[line]: return (1, (line, board[line].index("00.") + 2))
                if (board[line].count(str(i)) == len(board)/2) and "." in board[line]: return (1, (line, board[line].index(".")))
            elif i == 1:
                if ".11" in board[line]:   return (0, (line, board[line].index(".11")))
                elif "1.1" in board[line]: return (0, (line, board[line].index("1.1") + 1))
                elif "11." in board[line]: return (0, (line, board[line].index("11.") + 2))
                elif board[line].count(str(i)) == len(board)/2 and "." in board[line]: return (0, (line, board[line].index(".")))

# Update board ---------------------------------------------------------------------------------------------
def UpdateBoard(board, update):
    # Define variables
    line = []
    new_line = ""
    # create a list of all characters in the line that needs updating
    for char in board[update[1][0]]:
        line.append(char)
    # Update line with the found value at the correct position
    line[update[1][1]] = update[0]
    # convert line back to string
    for char in line:
        new_line += str(char)
    return new_line

# Check for duplicate rows/ columns ------------------------------------------------------------------------
def Identical(board):
    for i in range(len(board)):
        for row in board:
            if board[i] == row and board.index(row) != i:
                return False
            else:
                return True

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
board = []
for i in range(1, board_size + 1):
    row = input("Row {}: ".format(i))
    # Catching input errors -------------------------------------------------------------------------------
    while InputCheck(row):
        for error in InputCheck(row):
            print(error)
        row = input("Row {}: ".format(i))
    # SAVE INPUT INTO BOARD -------------------------------------------------------------------------------
    board.append(row)
# =========================================================================================================

# SOLVER ==================================================================================================
# Print original board ------------------------------------------------------------------------------------
print(board)

# Find certain values & update board with them ------------------------------------------------------------
while CountEmpty(board) != 0:
    # Rows
    row_value = Certain(board)
    if row_value:
        board[row_value[1][0]] = UpdateBoard(board, row_value)
    # Columns
    col_value = Certain(TransposeBoard(board))   
    if col_value:
        col_value = (col_value[0], (col_value[1][1], col_value[1][0]))
        board[col_value[1][0]] = UpdateBoard(board, col_value)
    # End loop
    if not row_value and not col_value:
        break

# Check for duplicate rows/ columns -----------------------------------------------------------------------
if Identical(board) and Identical(TransposeBoard(board)):
    print(board)
else:
    print("[Error] Duplicate rows/ columns found")

# 
# ========================================================================================================
"""

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