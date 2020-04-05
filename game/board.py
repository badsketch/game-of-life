from .cell import Cell

class Board:
    
    def __init__(self, num_rows, num_cols):
        self._nrows = num_rows
        self._ncols = num_cols
        self._board = [[Cell() for j in range(self._ncols)] for i in range(self._nrows)]

    def __str__(self):
        result = ''
        for i in range(self._nrows):
            for j in range(self._ncols):
                result += (str(self._board[i][j]))
                result += ' ' if j < self._ncols - 1 else ''
            result += '\n' if i < self._nrows - 1 else ''
        return result