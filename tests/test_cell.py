import unittest
from game.cell import Cell, CellState

class Test_Cell(unittest.TestCase):

    def test_print_cell(self):
        cell1 = Cell()
        self.assertEqual(str(cell1), CellState.DEAD)
        self.assertFalse(cell1.is_alive)
        cell2 = Cell(True)
        self.assertEqual(str(cell2), CellState.ALIVE)
        self.assertTrue(cell2.is_alive)

    def test_cell_can_die_and_live(self):
        cell = Cell(is_alive=True)
        self.assertEqual(str(cell), CellState.ALIVE)
        cell.die()
        self.assertEqual(str(cell), CellState.DEAD)
        cell.live()
        self.assertEqual(str(cell), CellState.ALIVE)
