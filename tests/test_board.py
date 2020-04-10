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

    def test_generates_board_from_matrix(self):
        matrix = [[0,0,0],[1,0,1],[1,1,1]]
        board = Board(3, 3, matrix)
        output = '◻ ◻ ◻\n◼︎ ◻ ◼︎\n◼︎ ◼︎ ◼︎'
        self.assertMultiLineEqual(str(board), output)

    def test_refreshes_board_square(self):
        board = Board(3,3)
        new_state = [[0,0,0],[1,0,1],[1,1,1]]
        output = '◻ ◻ ◻\n◼︎ ◻ ◼︎\n◼︎ ◼︎ ◼︎'
        board.set_new_state(new_state)
        self.assertMultiLineEqual(str(board), output)
    
    def test_sets_new_board_state_rect(self):
        board = Board(5,3)
        new_state = [[0,1,1],[1,1,1],[0,1,0],[0,0,0],[1,1,1]]
        output = '◻ ◼︎ ◼︎\n◼︎ ◼︎ ◼︎\n◻ ◼︎ ◻\n◻ ◻ ◻\n◼︎ ◼︎ ◼︎'
        board.set_new_state(new_state)
        self.assertMultiLineEqual(str(board), output)

    def test_sets_new_board_state_wrong_num_rows(self):
        board = Board(3,3)
        new_state = [[0,0,0],[1,0,1]]
        with self.assertRaisesRegex(Exception, 'new state does not match number of rows'):
            board.set_new_state(new_state)

    def test_sets_new_board_state_wrong_num_cols(self):
        board = Board(3,3)
        new_state_1 = [[0,0],[1,1],[1,1]]
        with self.assertRaisesRegex(Exception, 'new state does not match number of columns'):
            board.set_new_state(new_state_1)
        
        new_state_2 = [[0,0,0],[1,1],[1,1]]
        with self.assertRaisesRegex(Exception, 'new state does not match number of columns'):
            board.set_new_state(new_state_2)
    
        new_state_3 = [[0,0,0],[1,1,1],[1,1]]
        with self.assertRaisesRegex(Exception, 'new state does not match number of columns'):
            board.set_new_state(new_state_3)

    def test_calculates_next_board_state_1(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3, 3, seed_state)
        board.calculate_next_board_state()
        cycle_1 = '◻ ◻ ◻\n◻ ◻ ◻\n◻ ◻ ◻'
        self.assertMultiLineEqual(str(board), cycle_1)
        board.calculate_next_board_state()
        cycle_2 = '◻ ◻ ◻\n◻ ◻ ◻\n◻ ◻ ◻'
        self.assertMultiLineEqual(str(board), cycle_2)
        self.assertEqual(board._cycles, 2)

    def test_calculates_next_board_state_2(self):
        seed_state = [[1,0,0], [0,1,0], [1,1,1]]
        board = Board(3,3, seed_state)
        board.calculate_next_board_state()
        cycle_1 = '◻ ◻ ◻\n◻ ◻ ◼︎\n◼︎ ◼︎ ◼︎'
        self.assertMultiLineEqual(str(board), cycle_1)
        board.calculate_next_board_state()
        cycle_2 = '◻ ◻ ◻\n◻ ◻ ◼︎\n◻ ◼︎ ◼︎'
        self.assertMultiLineEqual(str(board), cycle_2)
        board.calculate_next_board_state()
        cycle_3 = '◻ ◻ ◻\n◻ ◼︎ ◼︎\n◻ ◼︎ ◼︎'
        self.assertMultiLineEqual(str(board), cycle_3)
        board.calculate_next_board_state()
        cycle_4 = '◻ ◻ ◻\n◻ ◼︎ ◼︎\n◻ ◼︎ ◼︎'
        self.assertMultiLineEqual(str(board), cycle_4)
        self.assertEqual(board._cycles, 4)


    def test_calculate_next_board_state_3(self):
        seed_state = [[1,1,1], [1,1,1], [1,1,1]]
        board = Board(3,3, seed_state)
        board.calculate_next_board_state()
        cycle_1 = '◼︎ ◻ ◼︎\n◻ ◻ ◻\n◼︎ ◻ ◼︎'
        self.assertMultiLineEqual(str(board), cycle_1)
        board.calculate_next_board_state()
        cycle_2 = '◻ ◻ ◻\n◻ ◻ ◻\n◻ ◻ ◻'
        self.assertMultiLineEqual(str(board), cycle_2)
        self.assertEqual(board._cycles, 2)


    

    
        


        

