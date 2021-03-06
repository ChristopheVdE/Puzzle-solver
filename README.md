# Puzzle solver

## Requires:
  - python
  - pygame

## Content:
<details>
<summary>Pygame application:</summary>
  
  - Working:
    - Main menu
    - Binairo game
    - Binairo Solver
    - Sudoku game
    - Sudoku Solver
    - Hudoku game
    - Hudoku Solver

</details>
<details>
<summary>Terminal only scripts:</summary>
  
  - script to solve sudoku's
  - script to solve binairo's
  - script to create binairo's
  
</details>
 
## Pygame application
<details>
<summary>Main menu</summary>
  
![Screenshot](./Readme_Images/MainMenu.png)

  - Choose the type of puzzle that you want to play
  - Get some info about the selected puzzle-type (picture, rules...)
  - "Play"-button: Play a randomly genereated puzzle
  - "Solve"-button: Imput a premade puzzleboard and let the app find the solution
  
</details>

<details>
<summary>Sudoku</summary>
  <details>
    <summary>Play/ Create</summary>
    
  - A random board will be automatically created
  - A new board can be created by pressing "New"*
  - The board can be resetted to it's original state
  - The "Hint"-button will fill in a random empty cube
  - The "Check"-button:
      - removes all wrong values from the board
      - gives all correct values a grey cube-background
      - disables selection of the correct values so that they cant be changed anymore.
  - automatic highlighting of the selcted cube, row and column
  
   </details>
  <details>
    <summary>Solve</summary>

The algorithm will search for a solution for the board. If the board has no valid solution it will display a message saying: "Impossible".
  
Usage:
  - Left mouse button: select a cube in which to add a value
  - Delete or "0": remove all values from the selected cube
  - Press "Solve" when you have created your test-board

   </details>
</details>  

<details>
<summary>Hudoku</summary>
  <details>
    <summary>Play/ Create</summary>
    
  - A random board will be automatically created
  - A new board can be created by pressing "New"*
  - The board can be resetted to it's original state
  - The "Hint"-button will fill in a random empty cube
  - The "Check"-button:
      - removes all wrong values from the board
      - gives all correct values a grey cube-background
      - disables selection of the correct values so that they cant be changed anymore.
  - automatic highlighting of the selcted cube, row and column
  
   </details>
  <details>
    <summary>Solve</summary>

The algorithm will search for a solution for the board. If the board has no valid solution it will display a message saying: "Impossible".
  
Usage:
  - Left mouse button: select a cube in which to add a value
  - Delete or "0": remove all values from the selected cube
  - Press "Solve" when you have created your test-board

   </details>
</details>  

<details>
<summary>Binairo</summary>
  <details>
    <summary>Play/ Create</summary>
    
  ![Screenshot](./Readme_Images/BinairoPlay.png)
  
  - A random board (10 cubes) will be automatically created*
  - A new board of the desired size (2 - 14 cubes) can be created by changing the value and pressing "New"*
  - The board can be resetted to it's original state
  - The "Hint"-button will fill in a random empty cube
  - The "Check"-button:
      - removes all wrong values from the board
      - gives all correct values a grey cube-background
      - disables selection of the correct values so that they cant be changed anymore.
  - automatic highlighting of the selcted cube, row and column
  
  Usage:
  
    - Left mouse button: select a cube in which to add a value of which you are certain
    - Right mouse button: select a cube in which to add TEMPORARY values (values of which you aren't certain)
    - Delete or ".": remove all values from teh selected cube

  Board generation can take a while depending on the selected board size.
    
   </details>
  <details>
    <summary>Solve</summary>
  
The algorithm will search for a solution for the board. If the board has no valid solution it will display a message saying: "Impossible".
  
Usage:
  - Left mouse button: select a cube in which to add a value
  - Delete or ".": remove all values from the selected cube
  - Press "Solve" when you have created your test-board

        
    
   </details>
</details>  
