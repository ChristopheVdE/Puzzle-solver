# SUDOKU SOLVER

# INPUT THE BOARD ======================================================================================
print(
    "\nINSTRUCTIONS:"
    "\n  - Please input the board (row by row) below"
    "\n  - Use a dot for an empty space"
    "\n  - Don't type separators between numbers"
    "\n  Example: 1101...001\n"
)
# # SET BOARD SIZE ---------------------------------------------------------------------------------------
# board = []
# board_size = input("Size of the board (needs to be an even number): ")
# while not board_size.isdigit() or int(board_size) % 2 != 0:
#     if board_size.isdigit():
#         if int(board_size) % 2 != 0:
#             print("[ERROR] board size must be an even number")
#     else:
#         print("[ERROR] Non-numeric characters found. Board size must be an even number")
#     board_size = input("Size of the board (needs to be an even number): ")
# board_size = int(board_size)

# # INPUT ROWS -------------------------------------------------------------------------------------------
# for i in range(1, board_size + 1):
#     line = input("Line {}: ".format(i))
#     # ERROR CHECKS -------------------------------------------------------------------------------------
#     while True:
#         errors = []
#         # CHECK IF INPUT MEETS REQUIRERED LENGHT -------------------------------------------------------
#         if len(line) != board_size:
#             if len(line) < board_size:
#                 errors.append(
#                     "[ERROR] Line is to short, a line must contain {} characters".format(
#                         board_size
#                     )
#                 )
#             else:
#                 errors.append(
#                     "[ERROR] Line is to long, a line must contain {} characters".format(
#                         board_size
#                     )
#                 )
#         # CHECK IF LINE CONTAINS MORE THEN 2 OF THE SAME CHARACTER NEXT TO EACHOTHER -------------------
#         if "000" in line or "111" in line:
#             errors.append(
#                 "[ERROR] To many instances of the same character (0 or 1) next to eachoter, only 2 instances of 0 or 1 are allowed next to eachoter."
#             )
#         # CHECK IF LINE CONTAINS UNWANTED CHARACTERS (lETTERS) -----------------------------------------
#         for j in line:
#             if j != "0" and j != "1" and j != ".":
#                 errors.append(
#                     '[ERROR] Unallowed charaters found, only "0", "1" and "." are allowed'
#                 )
#                 break
#         # CHECK IF LINE CONTAINS TO MANY INSTANCES OF A CERTAIN NUMBER ---------------------------------
#         for j in range(0, 2):
#             count = str(line).count("{}".format(j))
#             if count > (board_size / 2):
#                 errors.append(
#                     "[ERROR] Line can only contain {} instances of '{}': found {} instances of '{}'".format(
#                         int(board_size / 2), j, count, j
#                     )
#                 )
#                 break
#         # ERROR PRINTING -------------------------------------------------------------------------------
#         # NO ERRORS --> SKIP TO INPUT NEXT LINE
#         if len(errors) == 0:
#             break
#         # ERRORS FOUND --> PRINT ERRORS AND RE-INPUT CURRENT LINE
#         else:
#             for error in errors:
#                 print(error)
#             line = input("Line {}: ".format(i))
#     # SAVE INPUT INTO BOARD ----------------------------------------------------------------------------
#     row = []
#     for num in line:
#         row.append(num)
#     board.append(row)
# ======================================================================================================

board_size = 12
board = [
    [".", ".", ".", "1", ".", ".", ".", "1", ".", ".", "1", "."],
    [".", "0", ".", ".", "0", "1", ".", ".", ".", "0", ".", "."],
    [".", "0", ".", ".", ".", ".", ".", ".", ".", "0", "0", "."],
    [".", ".", "0", "0", ".", ".", ".", "0", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "0", ".", ".", ".", ".", "1"],
    [".", "1", ".", ".", ".", "1", ".", "1", ".", "0", ".", "."],
    [".", "1", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "0", ".", "0"],
    [".", "0", ".", ".", ".", "0", "0", ".", ".", ".", ".", "0"],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "1", "1", ".", ".", ".", "0", ".", ".", ".", ".", "0"],
    [".", ".", ".", "0", ".", "1", "0", ".", ".", ".", "1", "."],
]

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


# VALIDATION OF POSSIBLE VALUES------------------------------------------------------------------------------
def certain(board, board_size, empty_pos, proposed_val):
    # PREPARATION -------------------------------------------------------------------------------------------
    row_nr, col_nr = empty_pos
    proposed_val = str(proposed_val)
    # CONVERT ROW LIST TO STRING
    row = ""
    for i in board[row_nr]:
        row += str(i)
    # CONVERT COLUMN LIST TO STRING
    col = ""
    for i in column(board, col_nr):
        col += str(i)
    # AVOIDING TRIPLE VALUES IN ROW ----------------------------------------------------------------------------------------------
    if "00." in row and proposed_val != "0":
        index = row.index("00.") + 2
        return (row_nr, index)
    elif "11." in row and proposed_val != "1":
        index = row.index("11.") + 2
        return (row_nr, index)
    elif ".00" in row and proposed_val != "0":
        index = row.index(".00")
        return (row_nr, index)
    elif ".11" in row and proposed_val != "1":
        index = row.index(".11")
        return (row_nr, index)
    elif "0.0" in row and proposed_val != "0":
        index = row.index("0.0") + 1
        return (row_nr, index)
    elif "1.1" in row and proposed_val != "1":
        index = row.index("1.1") + 1
        return (row_nr, index)
    # AVOIDING TRIPPLE VALUES IN COLUMN --------------------------------------------------------------------------------------------
    elif "00." in col and proposed_val != "0":
        index = col.index("00.") + 2
        return (index, col_nr)
    elif "11." in col and proposed_val != "1":
        index = col.index("11.") + 2
        return (index, col_nr)
    elif ".00" in col and proposed_val != "0":
        index = col.index(".00")
        return (index, col_nr)
    elif ".11" in col and proposed_val != "1":
        index = col.index(".11")
        return (index, col_nr)
    elif "0.0" in col and proposed_val != "0":
        index = col.index("0.0") + 1
        return (index, col_nr)
    elif "1.1" in col and proposed_val != "1":
        index = col.index("1.1") + 1
        return (index, col_nr)
    # FILLING IN ROW IF ALL "0" OR "1" ARE FOUND ------------------------------------------------------------------------------------
    elif row.count("0") == board_size / 2 and proposed_val != "0":
        return empty_pos
    elif row.count("1") == board_size / 2 and proposed_val != "1":
        return empty_pos
    elif col.count("0") == board_size / 2 and proposed_val != "0":
        return empty_pos
    elif col.count("1") == board_size / 2 and proposed_val != "1":
        return empty_pos
    return False


# VALIDATION OF POSSIBLE VALUES: MAX INSTANCES OF 1 AND 2 PER ROW CHECK--------------------------------------
def check_max_instances(board, board_size, empty_pos, proposed_val, brute_force):
    if brute_force == False:
        # AVOID MORE INSTANCES OF SAME VALUE THAN ALLOW IN ROW
        if board[empty_pos[0]].count(proposed_val) + 1 > (board_size / 2):
            return False
        # AVOID MORE INSTANCES OF SAME VALUE THAN ALLOW IN COLUMN
        if column(board, empty_pos[1]).count(proposed_val) + 1 > (board_size / 2):
            return False
        return True
    else:
        # AVOID MORE INSTANCES OF SAME VALUE THAN ALLOW IN ROW
        if board[empty_pos[0]].count(proposed_val) > (board_size / 2):
            return False
        # AVOID MORE INSTANCES OF SAME VALUE THAN ALLOW IN COLUMN
        if column(board, empty_pos[1]).count(proposed_val) > (board_size / 2):
            return False
        return True


# VALIDATION OF POSSIBLE VALUES: CHEK IF PROPOSED VALUE CREATES IDENTICAL ROW/ COLUMNS -----------------------
def check_identical(board, board_size, empty_pos, proposed_val, brute_force):
    if brute_force == False:
        # insert the proposed value into the (test)-board to test if this creates duplicate rows/ columns
        board[empty_pos[0]][empty_pos[1]] == str(proposed_val)
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
def final_board_check(board, board_size, empty_pos, proposed_val):
    # board[empty_pos[0]][empty_pos[1]] = str(proposed_val)
    # PREPARATIONS ROW
    row_list = board[empty_pos[0]]
    row_list[empty_pos[1]] = str(proposed_val)
    row = ""
    for j in row_list:
        row += str(j)

    print("\nrow: " + row)
    # PREPARATIONS COL
    col = ""
    column_list = column(board, empty_pos[1])
    column_list[empty_pos[0]] = str(proposed_val)
    for j in column_list:
        col += str(j)
    print("col: " + col)

    # [ERROR CHECK] check row and column for triple values
    print(board)
    if not "000" in row and not "111" in row:
        print("no tripple row")
        if not "000" in col and not "111" in col:
            print("no tripple col")
            # CHECK IF THERE ARE TO MANY 0 OR 1 IN A ROW
            if str(row).count(str(proposed_val)) <= (board_size / 2):
                print("not to many row")
                # CHECK IF THERE ARE TO MANY 0 OR 1 IN A COLUMN
                if str(col).count(str(proposed_val)) <= (board_size / 2):
                    print("not to many col")
                    # CHECK FOR INDENTICAL ROWS AND COLUMNS
                    if check_identical(
                        board, board_size, empty_pos, str(proposed_val), True
                    ):
                        print("no identical")
                        return True
    return False


# BRUTE FORCE (RECURSIVE) ------------------------------------------------------------------------------
def brute_force(board, board_size):
    # FIND EMPTY POSITIONS ON BOARD --------------------------------------------------------------------
    empty = find_empty(board)
    if not empty:
        # solution found
        return True
    else:
        row_nr, col_nr = empty[0]

    for proposed_val in range(0, 2):
        proposed_val = str(proposed_val)
        # convert row list to a string
        row_list = board[row_nr]
        row = ""
        for val in row_list:
            row += str(val)
        # create duplicate list in which the poroposed value is inserted --> required for testing on tripple values
        row_list_value = row_list
        row_list_value[col_nr] = proposed_val
        row_value = ""
        for val in row_list_value:
            row_value += str(val)
        # print("row " + str(row_nr) + ": " + row_value)

        # convert col list to a string
        col_list = column(board, col_nr)
        col = ""
        for val in col_list:
            col += str(val)
        # create duplicate list in which the poroposed value is inserted --> required for testing on tripple values
        col_list_value = col_list
        col_list_value[row_nr] = proposed_val
        col_value = ""
        for val in col_list_value:
            col_value += str(val)
        # print("col " + str(col_nr) + ": " + col_value)

        if (
            not row.count(proposed_val) >= board_size
            and not col.count(proposed_val) >= board_size
            and not "000" in row_value
            and not "111" in row_value
            and not "000" in col_value
            and not "111" in col_value
            and check_identical(board, board_size, (row_nr, col_nr), proposed_val, True)
        ):
            board[row_nr][col_nr] = proposed_val

            if brute_force(board, board_size):
                return True
            else:
                board[row_nr][col_nr] = "."
    return False


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
            if certain(board, board_size, empty_pos, str(i)):
                position = certain(board, board_size, empty_pos, str(i))
                board[position[0]][position[1]] = str(i)

            # if valid(board, board_size, empty_pos, str(i)):
            #     board[empty_pos[0]][empty_pos[1]] = str(i)
            #     break
        # print_board(board)
        # print()
    # BREAK LOOP IF NO MORE VALID VALUES (NO BOARD UPDATES) --------------------------------------------
    if total_empty == len(find_empty(board)):
        break

print("before brute forcing")
print_board(board)

# BRUTE FORCE A SOLUTION -------------------------------------------------------------------------------
# if still empty values AND no more certain values
if len(find_empty(board)) != 0:
    # print("brute forcing")
    if brute_force(board, board_size):
        print("\nSolution:")
        print_board(board)


# CHECK FOR ERRORS IN FINAL BOARD
# errors = check(board, board_size)
# if len(errors) == 0:
#     print("new board")
#     print_board(board)
# else:
#     print("unsolvable:")
#     for error in errors:
#         print(error)
