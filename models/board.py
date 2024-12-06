class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        for i, row in enumerate(self.grid):
            print("|".join(row))
            # Only print the separator line if it's not the last row
            if i < len(self.grid) - 1:
                print("-" * 5)

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        # Check diagonals
        if self.grid[0][0] != " " and all(self.grid[i][i] == self.grid[0][0] for i in range(len(self.grid))):
            return self.grid[0][0]
        if self.grid[0][2] != " " and all(self.grid[i][2 - i] == self.grid[0][2] for i in range(len(self.grid))):
            return self.grid[0][2]

        # Check rows and columns
        for i in range(len(self.grid)):
            if self.grid[i][0] != " " and all(self.grid[i][j] == self.grid[i][0] for j in range(len(self.grid))):
                return self.grid[i][0]
            if self.grid[0][i] != " " and all(self.grid[j][i] == self.grid[0][i] for j in range(len(self.grid))):
                return self.grid[0][i]

        return ""  # No winner
        
    
    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)