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

    def test_calculates_next_board_state(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3, 3, seed_state)
        board.calculate_next_board_state()
        next_state_output = '◻ ◻ ◻\n◻ ◻ ◻\n◻ ◻ ◻'
        self.assertMultiLineEqual(str(board), next_state_output)

    # ------------------TEST GAME OF LIFE LOGIC-------------------------------------
    # underpopulation
    def test_calculate_next_state_for_index_underpopulation_0(self):
        seed_state = [[0,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_underpopulation_1(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))
    
    #overpopulation
    def test_calculate_next_state_for_index_overpopulation_4(self):
        seed_state = [[1,1,1],[1,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_overpopulation_5(self):
        seed_state = [[1,1,1],[1,1,1],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_overpopulation_6(self):
        seed_state = [[1,1,1],[1,1,1],[1,0,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_overpopulation_7(self):
        seed_state = [[1,1,1],[1,1,1],[1,1,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_overpopulation_8(self):
        seed_state = [[1,1,1],[1,1,1],[1,1,1]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_unchanged_2(self):
        seed_state = [[1,1,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertTrue(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_unchanged_3(self):
        seed_state = [[1,1,0],[0,1,1],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertTrue(board.calculate_next_state_for_index(1,1))

    def test_calculate_next_state_for_index_stays_dead_2(self):
        seed_state = [[1,1,0],[0,0,0],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertFalse(board.calculate_next_state_for_index(1,1))
    
    def test_calculate_next_state_for_index_lives_3(self):
        seed_state = [[1,1,0],[0,0,1],[0,0,0]]
        board = Board(3,3,seed_state)
        self.assertTrue(board.calculate_next_state_for_index(1,1))

    

    # ------------------TEST GET NEIGHBORS ------------------------------------
    def test_get_neighbors_for_index_regular(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(1,1)
        expected = [1,0,0,0,0,0,0,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    def test_get_neighbors_for_index_top_left_corner(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(0,0)
        expected = [0,1,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)
    
    def test_get_neighbors_for_index_top_middle(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(0,1)
        expected = [1,0,1,0,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    def test_get_neighbors_for_index_top_right_corner(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(0,2)
        expected = [0,1,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)
    
    def test_get_neighbors_for_index_middle_left(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(1,0)
        expected = [1,0,1,0,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    def test_get_neighbors_for_index_middle_left_nonsquare(self):
        seed_state = [[1,1,1],[0,1,0],[0,0,1],[1,1,1]]
        board = Board(4,3, seed_state)
        neighbors = board.get_neighbors_for_index(1,0)
        expected = [1,1,1,0,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    def test_get_neighbors_for_index_middle_right(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(1,2)
        expected = [0,0,1,0,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)


    def test_get_neighbors_for_index_bottom_left_corner(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(2,0)
        expected = [0,1,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    def test_get_neighbors_for_index_bottom_middle(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(2,1)
        expected = [0,0,1,0,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    def test_get_neighbors_for_index_bottom_right_corner(self):
        seed_state = [[1,0,0],[0,1,0],[0,0,0]]
        board = Board(3,3,seed_state)
        neighbors = board.get_neighbors_for_index(2,2)
        expected = [0,1,0]
        self.assertCountEqual([n.is_alive for n in neighbors if n], expected)

    

    
        


        

