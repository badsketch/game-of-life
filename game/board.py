import os
from time import sleep
from .cell import Cell

class Board:
    
    def __init__(self, matrix: list = None) -> None:
        self._cycles = 0
        self._nrows = len(matrix)
        self._ncols = len(matrix[0])
        if self._is_correct_shape(matrix):
            self._board = [[Cell() for j in range(self._ncols)] for i in range(self._nrows)]
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

    def calculate_next_board_state(self) -> None:
        new_state = [[False for j in range(self._ncols)] for i in range(self._nrows)]
        # calculate the next state for each index
        for i in range(self._nrows):
            for j in range(self._ncols):
                new_state[i][j] = self.calculate_next_state_for_index(i,j)
        self.set_new_state(new_state)
        self._cycles += 1

    def calculate_next_state_for_index(self, i: int, j: int) -> bool:
        neighbors = self.get_neighbors_for_index(i, j)
        live_count = len([n for n in neighbors if n.is_alive])
        if live_count < 2 or live_count > 3:
            return False
        else:
            if not self._board[i][j].is_alive and live_count == 2:
                return False
            else:
                return True

    # determines neighbors given index including edge cases
    def get_neighbors_for_index(self, row: int, col: int) -> list:
        neighbors = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self._nrows and 0 <= j < self._ncols and not(i == row and j == col):
                    neighbors.append(self._board[i][j])
        return neighbors

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

    # TODO
    def liven_at_index(self, row: int, col: int) -> None:
        self._board[row][col].die()

    # TODO
    def kill_at_index(self, row: int, col: int) -> None:
        self._board[row][col].live()

    def play(self) -> None:
        while True:
            self.calculate_next_board_state()
            print('CYCLE: ', self._cycles)
            print('\n')
            print(self.__str__())
            sleep(0.2)
            os.system('cls' if os.name == 'nt' else 'clear')

