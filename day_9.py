from common_functions import read_data
import numpy as np

def is_touching(head_y, head_x, tail_y, tail_x):
    diff = np.array([head_y-tail_y, head_x-tail_x])
    return diff

def round1(data, board_size=5):
    board = np.zeros(shape=(board_size, board_size))
    Y_DIM, X_DIM = board.shape
    head_y, head_x = Y_DIM, 0
    tail_y, tail_x = Y_DIM, 0

    for d in data:
        direc, dist = d.split(' ')
        match direc:
            case 'U':
                head_y -= int(dist)
            case 'D':
                head_y += int(dist)
            case 'L':
                head_x -= int(dist)
            case 'R':
                head_x += int(dist)
        print(direc, dist, (head_y, head_x))
        print(is_touching(head_y, head_x, tail_y, tail_x))

if __name__ == '__main__':
    data = read_data('./data/day_9_test.txt')
    round1(data)