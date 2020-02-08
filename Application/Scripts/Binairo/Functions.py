############################################################################################################
# NAME: Binairo
# AUTHOR: Christophe Van den Eynde
# FUNCTION: All scripts concerning Binairo's for the pygame apllication
############################################################################################################

# IMPORT PACKAGES ==========================================================================================
import pygame
import random
from Scripts.General.Classes import CenteredText
from Settings.Default import Colors, Fonts
# ==========================================================================================================

# Board ====================================================================================================
class board():
# Inititalize class ----------------------------------------------------------------------------------------
    def __init__(self, NumberOfCubes, StartPos):
        self.NumberOfCubes = int(NumberOfCubes)
        self.X = int(StartPos[0])
        self.Y = int(StartPos[1])
        self.CubeSize = 40
        self.spaceBetweenCubes = 1
        self.BoardSize = int((self.NumberOfCubes * self.CubeSize) + (self.NumberOfCubes * self.spaceBetweenCubes) + 2 + 4)
        self.selected = None
# Create empty board ---------------------------------------------------------------------------------------
    def CreateEmptyBoard(self):
        self.solution = []
        self.solvable = []
        self.immutable = []
        for row in range(self.NumberOfCubes):
            self.solution.append("{}".format('.' * self.NumberOfCubes))
            self.solvable.append("{}".format('.' * self.NumberOfCubes))
# [SOLVE] Prepare solving ----------------------------------------------------------------------------------
    def PrepareSolve(self):
        # Immutatble values = original values
        self.immutable = []
        for row in range(len(self.current)):
            for col in range(len(self.current)):
                if not self.current[row][col] == '.':
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
            if "000" in row or "111" in row or row.count('0') > self.NumberOfCubes / 2 or row.count('1') > self.NumberOfCubes / 2:
                return True
        for row in TransposeBoard(self.solution):
            if "000" in row or "111" in row or row.count('0') > self.NumberOfCubes / 2 or row.count('1') > self.NumberOfCubes / 2:
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
# [PLAY] Set correct board values as immutable & remove wrong values ---------------------------------------
    def Immutable(self):
        self.immutable = []
        for row in range(len(self.current)):
            for col in range(len(self.current)):
                if self.current[row][col] == self.solution[row][col]:
                    self.immutable.append((row, col))
                else:
                    if not isinstance(self.current[row][col], list):
                        self.current[row][col] = '.'
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
    def BoardBackground(self, Background):
        self.BoardSurface = pygame.Surface((self.BoardSize, self.BoardSize), pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
        self.BoardSurface.fill(Background)
# Draw the empty cubes -------------------------------------------------------------------------------------
    def DrawCubes(self, CubeColor, CorrectColor):
        # Parameters ---------------------------------------------------------------------------------------
        self.Rows = []      # contains start-coords and size of each row
        self.Cols = []      # contains start-coords and size of each column
        CubeX = 3  # border arround board = 2
        CubeY = 3  # border arround board = 2
        # Create cubes -------------------------------------------------------------------------------------
        for row in range(self.NumberOfCubes):
            if row == self.NumberOfCubes /2:        # thicker line in middle of board (horizontal)
                CubeY += 1
            for col in range(self.NumberOfCubes):
                if col == self.NumberOfCubes /2:    # thicker line in middle of board (vertical)
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
            if key != '.':
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
                tempValues = '.'
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
                if self.current[row][col] == '.':
                    Coords.append((row, col))
    # choose a random empty location to update -------------------------------------------------------------
        if len(Coords) != 0:
            tip = random.choice(Coords)
            self.current[tip[0]][tip[1]] = self.solution[tip[0]][tip[1]]
# Print Board ----------------------------------------------------------------------------------------------
    def PrintBoard(self, Screen):
    # Print values -----------------------------------------------------------------------------------------
        for row in range(len(self.Rows)):
            for col in range(len(self.Cols)):
                CubeCoords = (self.Cols[col][0], self.Rows[row][1])
            # Immutabe values ------------------------------------------------------------------------------
                if self.current[row][col] != "." and (row, col) in self.immutable:
                    value = CenteredText(self.current[row][col], Fonts["Immutable"], Colors["Immutable"], (CubeCoords[0] + self.CubeSize / 2), (CubeCoords[1] + self.CubeSize / 2))
                    value.render(self.BoardSurface)
            # New values -----------------------------------------------------------------------------------
                elif self.current[row][col] != "." and not isinstance(self.current[row][col], list) and not (row, col) in self.immutable:
                    value = CenteredText(self.current[row][col], Fonts["Certain"], Colors["Certain"], (CubeCoords[0] + self.CubeSize / 2), (CubeCoords[1] + self.CubeSize / 2))
                    value.render(self.BoardSurface)
            # Pencil ---------------------------------------------------------------------------------------
                elif isinstance(self.current[row][col], list) and not (row, col) in self.immutable:
                    # Coordinates for each value in pencil list
                    Coords = [
                        (int(CubeCoords[0] + self.CubeSize *5/6), int(CubeCoords[1] + self.CubeSize * 1/6)),
                        (int(CubeCoords[0] + self.CubeSize *5/6), int(CubeCoords[1] + self.CubeSize * 3/6))
                    ]
                    # Render
                    for i in range(len(self.current[row][col])):
                        value = CenteredText(self.current[row][col][i], Fonts["Pencil"], Colors["Pencil"], Coords[i][0], Coords[i][1])
                        value.render(self.BoardSurface)
    # Render BoardSurface on Main-Screen -------------------------------------------------------------------
        Screen.blit(self.BoardSurface, (self.X, self.Y))
# Check board ----------------------------------------------------------------------------------------------
    def CheckBoard(self, Screen, TitleFont, TitleColor):
        if self.current == self.solution and CountEmpty(self.current) == 0:
            Message = CenteredText("Solved", TitleFont, TitleColor, self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(Screen)
        elif self.current == self.solution and CountEmpty(self.current) != 0:
            Message = CenteredText("Impossible", TitleFont, TitleColor, self.X + self.BoardSize/ 2, self.Y + self.BoardSize / 2)
            Message.render(Screen)
# ==========================================================================================================

# FUNCTIONS ================================================================================================
# Transpose board to get columns ---------------------------------------------------------------------------
def TransposeBoard(BoardState):
    columns = []
    for column_nr in range(len(BoardState)):
        line = ''
        for row in BoardState:
            line += row[column_nr]
        columns.append(line)
    return columns

# Find empty -----------------------------------------------------------------------------------------------
def CountEmpty(BoardState):
    empty = 0
    for line in range(len(BoardState)):
        for char in BoardState[line]:
            if char == ".":
                empty += 1
    return empty

# Find certain values --------------------------------------------------------------------------------------
def Certain(BoardState):
    for line in range(len(BoardState)):
        for i in range(0, 2):
            if i == 0:
                if ".00" in BoardState[line]:
                    return (1, (line, BoardState[line].index(".00")))
                elif "0.0" in BoardState[line]:
                    return (1, (line, BoardState[line].index("0.0") + 1))
                elif "00." in BoardState[line]:
                    return (1, (line, BoardState[line].index("00.") + 2))
                elif (BoardState[line].count(str(i)) == len(BoardState) / 2) and "." in BoardState[line]:
                    return (1, (line, BoardState[line].index(".")))
            elif i == 1:
                if ".11" in BoardState[line]:
                    return (0, (line, BoardState[line].index(".11")))
                elif "1.1" in BoardState[line]:
                    return (0, (line, BoardState[line].index("1.1") + 1))
                elif "11." in BoardState[line]:
                    return (0, (line, BoardState[line].index("11.") + 2))
                elif BoardState[line].count(str(i)) == len(BoardState) / 2 and "." in BoardState[line]:
                    return (0, (line, BoardState[line].index(".")))

# Update board ---------------------------------------------------------------------------------------------
def UpdateBoard(BoardState, update):
    # Define variables
    new_line = ""
    # create a list of all characters in the line that needs updating
    line = list(BoardState[update[1][0]])
    # Update line with the found value at the correct position
    line[update[1][1]] = update[0]
    # convert line back to string
    for char in line:
        new_line += str(char)
    return new_line

# Update board with certain values
def UpdateCertain(BoardState):
        # Counter for ammount of certain values -------------------------------------------------------------------
    count_certain = 0

    # Find certain values & update board with them ------------------------------------------------------------
    while CountEmpty(BoardState) != 0:
        # Rows
        row_value = Certain(BoardState)
        if row_value:
            count_certain +=1
            BoardState[row_value[1][0]] = UpdateBoard(BoardState, row_value)
        # Columns
        col_value = Certain(TransposeBoard(BoardState))   
        if col_value:
            count_certain +=1
            col_value = (col_value[0], (col_value[1][1], col_value[1][0]))
            BoardState[col_value[1][0]] = UpdateBoard(BoardState, col_value) 
        # End loop if no cetain values where found
        if not row_value and not col_value:
            return BoardState, count_certain
    return BoardState, count_certain

# Check for duplicate rows/ columns ------------------------------------------------------------------------
def Identical(BoardState):
    for i in range(len(BoardState)):
        for row in BoardState:
            if BoardState[i] == row and BoardState.index(row) != i and not '.' in row:
                return False
    return True

# Brute force ----------------------------------------------------------------------------------------------
def BruteForce(BoardState):
    # Look for empty spots ---------------------------------------------------------------------------------
    if CountEmpty(BoardState) == 0:
        return BoardState
    else:
        for row in range(len(BoardState)):
            if "." in BoardState[row]:
                empty = (row, BoardState[row].index("."))
                original_row = BoardState[row]
                break
    # Try solution -----------------------------------------------------------------------------------------
    for value in random.choice([[0, 1], [1, 0]]):
        # Create new rows to test if the suggested value is valid
        new_row = UpdateBoard(BoardState, (value, empty))
        new_col = UpdateBoard(TransposeBoard(BoardState), (value, (empty[1], empty[0])))
        # Test if suggested value is valid
        if not "000" in new_row and not "111" in new_row and not "000" in new_col and not "111" in new_col:
            if not new_row.count(str(value)) > len(BoardState) / 2 and not new_col.count(str(value)) > len(BoardState) / 2:
                # Create test board to test for identical rows/ columns
                test_board = BoardState
                test_board[empty[0]] = new_row
                # Test for identical rows/ columns
                if Identical(test_board) and Identical(TransposeBoard(test_board)):
                    BoardState[empty[0]] = new_row
                    # try a value in the next empty position if a valid value was inserted, return true if value is possible
                    if BruteForce(BoardState):
                        return True
                    # reset value if next empty has no valid number
                    BoardState[row] = original_row
    # required for recursive, says that next empty has no valid number
    return False

# Create solvable state out of solution --------------------------------------------------------------------
def SolvableState(Solution):
    # Create list of coordinates in board ------------------------------------------------------------------
    coords = []
    for row in range(len(Solution)):
        for char in range(len(Solution[row])):
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
        TestBoard[position[0]] = UpdateBoard(TestBoard, (".", position))

        # Test if solution of board is still the same (stop board from having multiple solutions)
        TestBoard, count = UpdateCertain(TestBoard)
        
        if TestBoard == Solution:
            EmptiedBoard[position[0]] = UpdateBoard(EmptiedBoard, (".", position))

        # Remove tested position out of coordinates list
        del coords[index]
        
    # Return final board ----------------------------------------------------------------------------------------
    return EmptiedBoard

# Calculate the current percentage of empty values in the board --------------------------------------------
def Percentage(BoardState):
    Percentage = int(CountEmpty(BoardState) / (len(BoardState) * len(BoardState)) * 100)
    return Percentage
# ==========================================================================================================





