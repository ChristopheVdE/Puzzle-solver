############################################################################################################
# NAME: Sudoku
# AUTHOR: Christophe Van den Eynde
# FUNCTION: All scripts concerning Sudoku's for the pygame apllication
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
import random
from Scripts.General.Classes import CenteredText
# ==========================================================================================================

# Board ====================================================================================================
class board():
# Inititalize class ---------------------------------------------------------------------------------------
    def __init__(self, StartPos):
        self.NumberOfCubes = 9
        self.X = int(StartPos[0])
        self.Y = int(StartPos[1])
        self.CubeSize = 40
        self.spaceBetweenCubes = 1
        self.BoardSize = int((self.NumberOfCubes * self.CubeSize) + (self.NumberOfCubes * self.spaceBetweenCubes) + 2 + 5)
        self.selected = None
# Create empty board ---------------------------------------------------------------------------------------
    def CreateEmptyBoard(self):
        self.solution = []
        self.solvable = []
        self.immutable = []
        for row in range(self.NumberOfCubes):
            self.solution.append("{}".format('0' * self.NumberOfCubes))
            self.solvable.append("{}".format('0' * self.NumberOfCubes))
# [SOLVE] Prepare solving ----------------------------------------------------------------------------------
    def PrepareSolve(self):
        # Immutatble values = original values
        self.immutable = []
        for row in range(len(self.current)):
            for col in range(len(self.current)):
                if not self.current[row][col] == '0':
                    self.immutable.append((row, col))
        # Set self.solution equal to self.current (in string form)
        self.solution = []
        row = ''
        for line in self.current:
            for char in line:
                row += str(char)
            self.solution.append(row)
            row = ''
# [SOLVE] Look for errors ----------------------------------------------------------------------------------
    def Errors(self):
        for row in self.solution:
            for i in range(1,10):
                if row.count(str(i)) > 1:
                    return True
        for row in TransposeBoard(self.solution):
            for i in range(1,10):
                if row.count(str(i)) > 1:
                    return True
        return False
# [SOLVE] Solve the board: look for certain values ---------------------------------------------------------
    def FindCertain(self):
        self.solution, count = UpdateCertain(self.solution)
# Solve the board: Brute-forcing ---------------------------------------------------------------------------
    def BruteForce(self):
        BruteForce(self.solution)
# [SOLVE] Prepare board for printing -----------------------------------------------------------------------
    def PrepareRender(self):
        self.current = []
        for row in range(len(self.solution)):
            #self.current.append(list(row))
            self.current.append(list(self.solution[row]))
            self.solution[row] = list(self.solution[row])
# [PLAY] Create a random solvable boardstate ---------------------------------------------------------------
    def SolvableState(self):
    # Create solvable state out of solution
        self.solvable = SolvableState(self.solution)
    # Convert the rows of self.solution into lists --> for comparrisonwith self.current
        for row in range(len(self.solution)):
            self.solution[row] = list(self.solution[row])
# [PLAY] Create/reset the current board --------------------------------------------------------------------
    def CurrentBoard(self):
        self.current = []
        for row in self.solvable:
            self.current.append(list(str(row)))
# Set correct board values as immutable & remove wrong values ----------------------------------------------
    def Immutable(self):
        self.immutable = []
        for row in range(len(self.current)):
            for col in range(len(self.current)):
                if self.current[row][col] == self.solution[row][col]:
                    self.immutable.append((row, col))
                else:
                    if not isinstance(self.current[row][col], list):
                        self.current[row][col] = '0'
# Calculate center -----------------------------------------------------------------------------------------
    def CenterRectangle(self, ScreenWidth, ScreenHeight, Unoccupy_X, Unoccupy_Y):
        # Calcualte centered X
        self.X = self.X / 2 - self.BoardSize / 2
        while self.X + self.BoardSize > ScreenWidth - Unoccupy_X:
            self.X = self.X - (self.CubeSize + 1)
        # Calcualte centered Y
        self.Y = self.Y / 2 - self.BoardSize / 2
        while self.Y + self.BoardSize > ScreenHeight - Unoccupy_Y:
            self.Y = self.Y - (self.CubeSize + 1)
# Create board surface and fill it (background) ------------------------------------------------------------
    def BoardBackground(self, BackgroundColor):
        self.BoardSurface = pygame.Surface((self.BoardSize, self.BoardSize), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.BoardSurface.fill(BackgroundColor)
# Draw the empty cubes -------------------------------------------------------------------------------------
    def DrawCubes(self, CubeColor, CorrectColor):
        # Parameters ---------------------------------------------------------------------------------------
        self.Rows = []      #contains start-coords and size of each row
        self.Cols = []      #contains start-coords and size of each column
        CubeX = 3  #border arround board = 2
        CubeY = 3  #border arround board = 2
        # Create cubes -------------------------------------------------------------------------------------
        for row in range(self.NumberOfCubes):
            if row in [3, 6]:                       # 3x3 grid separation lines: rows (Sudoku)
                CubeY += 1
            for col in range(self.NumberOfCubes):   # 3x3 grid separation lines: columns (Sudoku)
                if col in [3, 6]:
                    CubeX += 1
            # Draw cubes ------------------------------------------------------------------------------------
                if (row, col) in self.immutable:    # Value is correct --> dark background, light font
                    pygame.draw.rect(self.BoardSurface, CorrectColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
                else:                               # Value is wrong --> light background, dark font
                    pygame.draw.rect(self.BoardSurface, CubeColor, (CubeX, CubeY, self.CubeSize, self.CubeSize))
            # Save coords of colum --------------------------------------------------------------------------
                if len(self.Cols) < self.NumberOfCubes:
                    self.Cols.append((CubeX, 3))
                CubeX += self.CubeSize + self.spaceBetweenCubes
            # Save coords of Row ----------------------------------------------------------------------------
            self.Rows.append((3, CubeY))
            # Reset positions for new row -------------------------------------------------------------------
            CubeX = 3
            CubeY += self.CubeSize + self.spaceBetweenCubes
# Highlight row & col of the location of the mouse ---------------------------------------------------------
    def HiglightLines(self, HighlightColor, mouse):
        # Create new surfaces for the higlights
        RowSurface = pygame.Surface((self.BoardSize -6, self.CubeSize))
        ColSurface = pygame.Surface((self.CubeSize, self.BoardSize -6))
        # Set color of highlights
        RowSurface.fill(HighlightColor)
        ColSurface.fill(HighlightColor)
        # Set alpha value of highlights (transparancy)
        RowSurface.set_alpha(50)
        ColSurface.set_alpha(50)
        # Check if mouse is in column-area & higlight column if true
        for col in self.Cols:
            if self.X + col[0] + self.CubeSize > mouse[0] > self.X + col[0] - 1 and self.Y + col[1] + self.BoardSize - 6 > mouse[1] > self.Y + col[1] - 1:
                self.BoardSurface.blit(ColSurface, (col[0], col[1]))
        # Check if mouse is in row-area & higlight row if true
        for row in self.Rows:
            if self.X + row[0] + self.BoardSize -6 > mouse[0] > self.X + row[0] -1 and self.Y + row[1] + self.CubeSize> mouse[1] > self.Y + row[1] -1:
                self.BoardSurface.blit(RowSurface, (row[0], row[1]))
# Return selected cube -------------------------------------------------------------------------------------
    def SelectCube(self, mouse, click):
        for row in range(len(self.Rows)):
            for col in range(len(self.Cols)):
                if not (row, col) in self.immutable:
                    if self.X + self.Cols[col][0] + self.CubeSize > mouse[0] > self.X + self.Cols[col][0] and self.Y + self.Rows[row][1] + self.CubeSize > mouse[1] > self.Y + self.Rows[row][1]:
                        # left mouse to wright a value
                        if click[0] == 1:
                            BoardPos = (row, col)
                            CubeCoords = (self.Cols[col][0], self.Rows[row][1])
                            self.selected = ("L", BoardPos, CubeCoords)
                        elif click[2] == 1:
                            BoardPos = (row, col)
                            CubeCoords = (self.Cols[col][0], self.Rows[row][1])
                            self.selected = ("R", BoardPos, CubeCoords)
        if self.selected:
            if not self.X + self.selected[2][0] + self.CubeSize > mouse[0] > self.X + self.selected[2][0] and not self.Y + self.selected[2][1] + self.CubeSize > mouse[0] > self.Y + self.selected[2][1]:
                self.selected = None
# [PLAY] Pencil values for the selected cube (temp values)--------------------------------------------------
    def Pencil(self, key=None):
        # Pencil in values ---------------------------------------------------------------------------------
        if self.selected and self.selected[0] == "R" and key:
            if key != '0':
            # Create list of temp values -------------------------------------------------------------------
                if not isinstance(self.current[self.selected[1][0]][self.selected[1][1]], list):
                    tempValues = []
                else:
                    tempValues = self.current[self.selected[1][0]][self.selected[1][1]]
            # Add temp values to list ----------------------------------------------------------------------
                if not key in tempValues:
                    tempValues.append(str(key))
                else:
                    tempValues.remove(str(key))
                tempValues.sort()
            # Remove all temp values if delete is pressed --------------------------------------------------
            else:
                tempValues = '0'
            # Update board ---------------------------------------------------------------------------------
            self.current[self.selected[1][0]][self.selected[1][1]] = tempValues
# Update value of the selected cube (certain values) -------------------------------------------------------
    def Updatecube(self, key=None):
        # Update value of selected cube if key is pressed
        if self.selected and self.selected[0] == "L" and key:
            self.current[self.selected[1][0]][self.selected[1][1]] = str(key)
# [PLAY] Give hint -----------------------------------------------------------------------------------------
    def Hint(self):
    # get list of all empty locations ----------------------------------------------------------------------
        Coords = []
        for row in range(self.NumberOfCubes):
            for col in range(self.NumberOfCubes):
                if self.current[row][col] == '0':
                    Coords.append((row, col))
    # choose a random empty location to update -------------------------------------------------------------
        if len(Coords) != 0:
            tip = random.choice(Coords)
            self.current[tip[0]][tip[1]] = self.solution[tip[0]][tip[1]]
# Print Board ----------------------------------------------------------------------------------------------
    def PrintBoard(self, Screen):
    # Fonts & Colors ---------------------------------------------------------------------------------------
        # immutable values
        ImmutableFont = pygame.font.Font('freesansbold.ttf', 20)
        ImmutableColor = (0,0,0)
        # Certain values:
        CertainFont = pygame.font.Font('freesansbold.ttf', 20)
        CertainColor = (0, 0, 0)
        # Pencil values
        PencilFont = pygame.font.Font('freesansbold.ttf', 10)
        PencilColor = (0, 0, 0)
    # Print values -----------------------------------------------------------------------------------------
        for row in range(len(self.Rows)):
            for col in range(len(self.Cols)):
                CubeCoords = (self.Cols[col][0], self.Rows[row][1])
            # Immutabe values ------------------------------------------------------------------------------
                if self.current[row][col] != "0" and (row, col) in self.immutable:
                    value = CenteredText(self.current[row][col], ImmutableFont, ImmutableColor, (CubeCoords[0] + self.CubeSize / 2), (CubeCoords[1] + self.CubeSize / 2))
                    value.render(self.BoardSurface)
            # New values -----------------------------------------------------------------------------------
                elif self.current[row][col] != "0" and not isinstance(self.current[row][col], list) and not (row, col) in self.immutable:
                    value = CenteredText(self.current[row][col], CertainFont, CertainColor, (CubeCoords[0] + self.CubeSize / 2), (CubeCoords[1] + self.CubeSize / 2))
                    value.render(self.BoardSurface)
            # Pencil ---------------------------------------------------------------------------------------
                elif isinstance(self.current[row][col], list) and not (row, col) in self.immutable:
                    # Coordinates for each value in pencil list
                    Coords = [
                        (int(CubeCoords[0] + self.CubeSize * 5/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize * 5/6), int(CubeCoords[1] + self.CubeSize * 3/6)),
                        (int(CubeCoords[0] + self.CubeSize * 5/6), int(CubeCoords[1] + self.CubeSize * 5/6)),
                        (int(CubeCoords[0] + self.CubeSize * 3/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize * 3/6), int(CubeCoords[1] + self.CubeSize * 3/6)),
                        (int(CubeCoords[0] + self.CubeSize * 3/6), int(CubeCoords[1] + self.CubeSize * 5/6)),
                        (int(CubeCoords[0] + self.CubeSize * 1/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize * 1/6), int(CubeCoords[1] + self.CubeSize * 3/6)),
                        (int(CubeCoords[0] + self.CubeSize * 1/6), int(CubeCoords[1] + self.CubeSize * 5/6))
                    ]
                    # Render
                    for i in range(len(self.current[row][col])):
                        value = CenteredText(self.current[row][col][i], PencilFont, PencilColor, Coords[i][0], Coords[i][1])
                        value.render(self.BoardSurface)
    # Render BoardSurface on Main-Screen -------------------------------------------------------------------
        Screen.blit(self.BoardSurface, (self.X, self.Y))
# Check board ----------------------------------------------------------------------------------------------
    def CheckBoard(self, Screen, TitleFont, TitleColor):
        if self.current == self.solution and len(find_empty(self.current)) == 0:
            Message = CenteredText("Solved", TitleFont, TitleColor, self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(Screen)
        elif self.current == self.solution and len(find_empty(self.current)) != 0:
            Message = CenteredText("Impossible", TitleFont, TitleColor, self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(Screen)
# ==========================================================================================================

# FUNCTIONS ================================================================================================
# Find all empty positions and return them in a list--------------------------------------------------------
def find_empty(board):
    empty_values = []
    for row in range(9):
        for char in range(9):
            if board[row][char] == "0":
                empty_values.append((row, char))
    return empty_values

# Return a list of all the values from the column of the selected position ---------------------------------
def column(board, col):
    column_values = []
    for row in board:
        column_values.append(row[col])
    return column_values

# Return a list of all the values from the 3x3 box that the selected position is part of -------------------
def box(board, empty_pos):
    # search 3x3 box
    box_x = empty_pos[0] // 3
    box_y = empty_pos[1] // 3
    # make list of values in box
    box_values = []
    for col in range(box_x * 3, box_x * 3 + 3):
        for row in range(box_y * 3, box_y * 3 + 3):
            box_values.append(board[col][row])
    return box_values

# Return all valid options for the selected position -------------------------------------------------------
def valid(board, empty_pos):
    valid = []
    for value in range(1, 10):
        if (
            not str(value) in board[empty_pos[0]]                # row
            and not str(value) in column(board, empty_pos[1])    # column
            and not str(value) in box(board, empty_pos)          # box
        ):
            valid.append(value)
    return valid

# Update board ---------------------------------------------------------------------------------------------
def UpdateBoard(BoardState, position,  update):        # update = (value, (X, y))
    # Define variables
    new_line = ""
    # Convert the row of the selected position into a list
    line = list(BoardState[position[0]])
    # Update list with the found value at the correct position
    line[position[1]] = update[0]
    # convert line back to string
    for char in line:
        new_line += str(char)
    return new_line

# look for positions that have only 1 valid option and update the board with those -------------------------
def UpdateCertain(BoardState):
    count = 0
    while len(find_empty(BoardState)) != 0:
        og_board = BoardState
        for empty_pos in find_empty(BoardState):
            values = valid(BoardState, empty_pos)
            if len(values) == 1:
                BoardState[empty_pos[0]] = UpdateBoard(BoardState, empty_pos, values)
                count +=1
        # Break looop if no more cerrain values are found
        if og_board == BoardState:
            return BoardState, count


# Brute force a solution -----------------------------------------------------------------------------------
def BruteForce(board):
    # Find empty positions --------------------------------------------------------------------
    all_empty = find_empty(board)
    if not all_empty:
        # solution found
        return True
    else:
        # Add randomness
        for empty_pos in all_empty:
            values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            random.shuffle(values)
        # CHECK POSSIBLE VALUES FOR EMPTY POSITION & UPDATE BOARD IF FOUND ---------------------------------
            for value in values:
                # search row, column and box
                if (
                    not value in board[empty_pos[0]]  # row
                    and not value in column(board, empty_pos[1])  # column
                    and not value in box(board, empty_pos)  # box
                ):
                    # update board if value is valid
                    board[empty_pos[0]] = UpdateBoard(board, empty_pos, value)
                    # try a value in the next empty position if a valid value was inserted, return true if value is possible
                    if BruteForce(board):
                        return True
                    # reset value if next empty has no valid number
                    board[empty_pos[0]] = UpdateBoard(board, empty_pos, "0")
            # required for recursive, says that next empty has no valid number
            return False

# Solvable state -------------------------------------------------------------------------------------------
def SolvableState(Solution):
    # Create list of coordinates in board ------------------------------------------------------------------
    coords = []
    for row in range(9):
        for char in range(9):
            coords.append((row, char))

    # Create duplicate boards for testing ------------------------------------------------------------------
    EmptiedBoard = []
    for i in Solution:
        EmptiedBoard.append(i)

    # Loop through coordinates and see if removal of value at coord still gives same solution of board ----------
    while len(coords) != 0:
        # Choose a random position out of coordinates & index of said position in the list of coordinates
        position = random.choice(coords)
        index = coords.index(position)

        # Create duplicate of the emptied board (used for solving and comparing solution to original solution)
        TestBoard = []
        for i in EmptiedBoard:
            TestBoard.append(i)

        # Update testboard with empty value
        TestBoard[position[0]] = UpdateBoard(TestBoard, position, "0")

        # Test if solution of board is still the same (stop board from having multiple solutions)
        TestBoard, count = UpdateCertain(TestBoard)
        
        if TestBoard == Solution:
            EmptiedBoard[position[0]] = UpdateBoard(EmptiedBoard, position, "0")

        # Remove tested position out of coordinates list
        del coords[index]
        
    # Return final board ----------------------------------------------------------------------------------------
    return EmptiedBoard



# Transpose board to get columns ---------------------------------------------------------------------------
def TransposeBoard(BoardState):
    columns = []
    for column_nr in range(len(BoardState)):
        line = ''
        for row in BoardState:
            line += row[column_nr]
        columns.append(line)
    return columns