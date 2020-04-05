import unittest
from game.board import Board
unittest.util._MAX_LENGTH=2000

class Test_Board(unittest.TestCase):

    def test_generates_board(self):
        square_board = Board(2,2)
        output = '◻ ◻\n◻ ◻'
        self.assertMultiLineEqual(str(square_board), output)
        rectangular_board_1 = Board(3,2)
        output_1 = '◻ ◻\n◻ ◻\n◻ ◻'
        self.assertMultiLineEqual(str(rectangular_board_1), output_1)
        rectangular_board_2 = Board(2,3)
        output_2 = '◻ ◻ ◻\n◻ ◻ ◻'
        self.assertMultiLineEqual(str(rectangular_board_2), output_2)

