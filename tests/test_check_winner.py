import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    
    def test_x_wins_row(self):
        board = Board()  # Initialize without passing a grid
        board.grid = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]  # Manually set the grid
        winner = board.check_winner()
        self.assertEqual(winner, "X")
    
    def test_o_wins_column(self):
        board = Board()
        board.grid = [["X", "O", " "], ["X", "O", " "], [" ", "O", " "]]
        winner = board.check_winner()
        self.assertEqual(winner, "O")
    
    def test_x_wins_diagonal(self):
        board = Board()
        board.grid = [["X", "O", " "], ["O", "X", " "], [" ", " ", "X"]]
        winner = board.check_winner()
        self.assertEqual(winner, "X")
    
    def test_no_winner(self):
        board = Board()
        board.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        winner = board.check_winner()
        self.assertEqual(winner, "")
    
    def test_no_winner_full_board(self):
        board = Board()
        board.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        winner = board.check_winner()
        self.assertEqual(winner, "")

if __name__ == "__main__":
    unittest.main()