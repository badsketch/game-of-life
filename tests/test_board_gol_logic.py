import unittest
from game.board import Board

class Test_GOL_Logic(unittest.TestCase):

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