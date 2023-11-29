def isValid(x, y, n, board):
    # Check if a number 'n' can be placed at position (x, y) in the Sudoku board.
    for i in range(9):
        # Check if 'n' is in the same row.
        if board[x][i] == n:
            return False
        # Check if 'n' is in the same column.
        if board[i][y] == n:
            return False
        # Check if 'n' is in the same 3x3 subgrid.
        if board[3 * (x // 3) + i // 3][3 * (y // 3) + i % 3] == n:
            return False
    # Return True if 'n' can be placed at position (x, y).
    return True

def solver(board):
    # Iterate over each cell in the Sudoku board.
    for x in range(9):
        for y in range(9):
            # Check if the cell is empty (denoted by 0).
            if board[x][y] == 0:
                # Try to fill the cell with a valid number (1-9).
                for i in range(1, 10):
                    # Check if the number 'i' can be placed at (x, y).
                    if isValid(x, y, i, board):
                        board[x][y] = i
                        # Recursively call solver to solve the rest of the board.
                        if solver(board):
                            return True  # If the board is solved, return True.
                        # If placing 'i' does not lead to a solution, reset the cell.
                        board[x][y] = 0
                # Backtrack if no valid number is found for this cell.
                return False
    # Return True if no empty cells are left, indicating the puzzle is solved.
    return True

def get_user_input():
    # Initialize an empty Sudoku grid.
    grid = []
    print("Enter your Sudoku grid, row by row. Use 0 for empty cells.")

    # Iterate over each row.
    for i in range(9):
        while True:
            # Get user input for each row.
            row_input = input(f"Enter row {i + 1} (9 numbers, separated by spaces): ")

            # Split the input string into a list and convert each element to an integer.
            row = row_input.split()
            if len(row) != 9:
                print("Invalid input. Please enter exactly 9 numbers for each row.")
                continue

            try:
                row = [int(num) for num in row]
                # Validate that each number is between 0 and 9.
                if all(0 <= num <= 9 for num in row):
                    grid.append(row)
                    break
                else:
                    print("Invalid number. Each number must be between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter only numbers.")

    return grid

# Get user input to fill the Sudoku grid.
user_grid = get_user_input()

# Solve the Sudoku puzzle.
solver(user_grid)

# Print the solved puzzle.
print("Solved Sudoku:")
for row in user_grid:
    print(row)

"""Test case
grid = [[3,9,0,8,0,0,0,0,0],
        [4,1,0,0,0,0,3,7,8],
        [0,0,0,7,3,2,0,4,0],
        [7,0,4,0,0,9,0,0,1],
        [1,0,8,0,4,5,0,2,7],
        [0,0,5,1,8,0,0,0,3],
        [0,8,0,0,5,1,0,9,0],
        [2,0,0,0,0,3,8,0,0],
        [0,7,1,9,0,0,6,3,0]]

# Solve the Sudoku puzzle.
solver(grid)

# Print the solved puzzle.
print(grid)"""