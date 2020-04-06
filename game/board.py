from .cell import Cell

class Board:
    
    def __init__(self, num_rows: int, num_cols: int, matrix: list = None) -> None:
        self._nrows = num_rows
        self._ncols = num_cols
        self._board = [[Cell() for j in range(self._ncols)] for i in range(self._nrows)]
        if matrix and self._is_correct_shape(matrix):
            for i in range(self._nrows):
                for j in range(self._ncols):
                    if matrix[i][j]:
                        self._board[i][j] = Cell(is_alive=True)
                    else:
                        self._board[i][j] = Cell()

    def __str__(self) -> None:
        result = ''
        for i in range(self._nrows):
            for j in range(self._ncols):
                result += (str(self._board[i][j]))
                result += ' ' if j < self._ncols - 1 else ''
            result += '\n' if i < self._nrows - 1 else ''
        return result

    def set_new_state(self, new_state: list) -> None:
        if self._is_correct_shape(new_state):
            for i in range(len(new_state)):
                for j in range((len(new_state[0]))):
                    if new_state[i][j]:
                        self._board[i][j].live()
                    else:
                        self._board[i][j].die()
        
    # validation helper for setting new state
    def _is_correct_shape(self, new_state: list) -> bool:
        if len(new_state) != self._nrows:
            raise Exception('new state does not match number of rows')
        
        for row in range(len(new_state)):
            if len(new_state[row]) != self._ncols:
                raise Exception('new state does not match number of columns')
        
        return True