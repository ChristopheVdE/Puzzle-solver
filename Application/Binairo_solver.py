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
            if board[i] == row and board.index(row) != i and not '.' in row:
                return False
    return True

# Brute force ----------------------------------------------------------------------------------------------
def BruteForce(board):
    # Look for empty spots ---------------------------------------------------------------------------------
    if CountEmpty(board) == 0:
        return board
    else:
        for row in range(len(board)):
            if "." in board[row]:
                empty = (row, board[row].index("."))
                original_row = board[row]
                break
    # Try solution -----------------------------------------------------------------------------------------
    for value in range(0, 2):
        # Create new rows to test if the suggested value is valid
        new_row = UpdateBoard(board, (value, empty))
        new_col = UpdateBoard(TransposeBoard(board), (value, (empty[1], empty[0])))
        # print(new_col)
        # Test if suggested value is valid
        if not "000" in new_row and not "111" in new_row and not "000" in new_col and not "111" in new_col:
            if not new_row.count(str(value)) > len(board) / 2 and not new_col.count(str(value)) > len(board) / 2:
                # Create test board to test for identical rows/ columns
                test_board = board
                test_board[empty[0]] = new_row
                # Test for identical rows/ columns
                if Identical(test_board):
                    board[empty[0]] = new_row
                    # try a value in the next empty position if a valid value was inserted, return true if value is possible
                    if BruteForce(board):
                        return True
                    # reset value if next empty has no valid number
                    board[row] = original_row
    # required for recursive, says that next empty has no valid number
    return False

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
    row = input("Row {}:\t".format(i))
    # Catching input errors -------------------------------------------------------------------------------
    while InputCheck(row):
        for error in InputCheck(row):
            print(error)
        row = input("Row {}:\t".format(i))
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
    print("Certain values:")
    print(board)
    # Brute force -----------------------------------------------------------------------------------------
    if CountEmpty(board) != 0:
        print("\nBrute forcing")
        if BruteForce(board):
            print("\nSolution:")
            print(board)
        else:
            print("\nImpossible")
else:
    print("[Error] Duplicate rows/ columns found")

# ========================================================================================================
