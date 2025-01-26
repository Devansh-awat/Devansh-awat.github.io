# Sudoku Solver

This is a web-based Sudoku Solver that allows you to input a Sudoku puzzle and get the solution instantly. The solver uses a backtracking algorithm to find the solution.

## Features

- Input Sudoku puzzles directly into the grid.
- Solve the puzzle with a single click.
- Highlights the original puzzle numbers in red.

## How to Use

1. Open https://devansh-awat.github.io/tools/Sudoku_solver/ in your web browser.
2. Enter the Sudoku puzzle numbers into the grid. Use `0` for empty cells.
3. Click the "Solve" button to get the solution.
4. The solution will be displayed in the grid below the input grid.

## Files

- `index.html`: The main HTML file containing the Sudoku solver interface and logic.
- `README.md`: This file.

## Algorithm

The solver uses a backtracking algorithm to solve the Sudoku puzzle. It recursively tries numbers in empty cells and checks if the current configuration is valid. If it finds a valid configuration, it continues; otherwise, it backtracks and tries the next number.

## Styling

The interface is styled using CSS to provide a clean and user-friendly experience. The grid lines are highlighted to make it easier to see the 3x3 subgrids.