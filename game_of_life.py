from game.board import Board

seed = []

with open('./seeds/glider.txt', 'r') as f:
    for line in f.readlines():
        seed.append([int(cell) for cell in line.rstrip().split(' ')])

print(seed)
board = Board(10,10,seed)
board.play()

