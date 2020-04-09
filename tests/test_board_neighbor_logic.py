import unittest
from game.board import Board

class Test_Get_Neighbors(unittest.TestCase):

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

    
