from game.board import Board

seed = []

with open('./seeds/gun.txt', 'r') as f:
    for line in f.readlines():
        seed.append([int(cell) for cell in line.rstrip().split(' ')])

board = Board(3,3,seed)
board.play()

