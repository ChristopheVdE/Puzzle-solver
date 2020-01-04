############################################################################################################
# NAME: BINAIRO Creator
# AUTHOR: Christophe Van den Eynde
# FUNCTION: creates a random solvable Binairo-type puzzle
# USAGE python binairo_creator.py
############################################################################################################

# PACKAGES =================================================================================================
import random
# ==========================================================================================================

# FUNCTIONS ================================================================================================
# Print Board ----------------------------------------------------------------------------------------------
def PrintBoard(board):
    row_count = 0
    for row in range(len(board)):
        line = []
        char_count = 0
        # Print board middle separator (horizontal)
        if row_count == len(board) / 2:
            print("{0}|{0}".format("-" * int(len(board) + 1)))
        # loop through row & print values
        for char in board[row]:
            #Add extra space in front of each line
            if char_count == 0:
                print(' ', end="")
            # Print board middle separator (vertical)
            if char_count == len(board) / 2:
                print("| ", end="")
            # Print values
            print("{} ".format(char), end="")
            char_count += 1
        # Print end of line
        print()
        row_count += 1
    # Add empty line after each printed board
    print()

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
                if ".00" in board[line]:
                    return (1, (line, board[line].index(".00")))
                elif "0.0" in board[line]:
                    return (1, (line, board[line].index("0.0") + 1))
                elif "00." in board[line]:
                    return (1, (line, board[line].index("00.") + 2))
                elif (board[line].count(str(i)) == len(board) / 2) and "." in board[line]:
                    return (1, (line, board[line].index(".")))
            elif i == 1:
                if ".11" in board[line]:
                    return (0, (line, board[line].index(".11")))
                elif "1.1" in board[line]:
                    return (0, (line, board[line].index("1.1") + 1))
                elif "11." in board[line]:
                    return (0, (line, board[line].index("11.") + 2))
                elif board[line].count(str(i)) == len(board) / 2 and "." in board[line]:
                    return (0, (line, board[line].index(".")))

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
    for value in random.choice([[0, 1], [1, 0]]):
        # Create new rows to test if the suggested value is valid
        new_row = UpdateBoard(board, (value, empty))
        new_col = UpdateBoard(TransposeBoard(board), (value, (empty[1], empty[0])))
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
# ===========================================================================================================

# CREATE RANDOM BOARD =======================================================================================
# Create empty placeholder board ----------------------------------------------------------------------------
board = []
for row in range(board_size):
    board.append("{}".format('.'*board_size))

# Create random solved board --------------------------------------------------------------------------------
BruteForce(board)
PrintBoard(board)

# Remove values from board ----------------------------------------------------------------------------------
# ===========================================================================================================