from common_functions import read_data
import numpy as np

def get_diff(hy, hx, ty, tx):
    diff = np.array([hy-hx, ty-tx])
    return diff

def touching(difference):
    difference = np.abs(difference)
    return not np.any(difference>1)

def move_tail(ty, tx, difference, board):
    # determine difference between head and tail

    # move smallest dimension first (if diagonal)
    smallest = np.where(difference==np.min(difference))
    print(smallest)
    # add visited squares to board

    # update tail y and x

    return

def round1(data, board_size=5):
    board = np.zeros(shape=(board_size, board_size))
    Y_DIM, X_DIM = board.shape
    head_y, head_x = Y_DIM-1, 0
    tail_y, tail_x = Y_DIM-1, 0

    for d in data:
        direc, dist = d.split(' ')
        print(direc, dist)
        match direc:
            case 'U':
                head_y -= int(dist)
            case 'D':
                head_y += int(dist)
            case 'L':
                head_x -= int(dist)
            case 'R':
                head_x += int(dist)
        difference = get_diff(head_y, head_x, tail_y, tail_x)
        print(difference)
        if not touching(difference):
            move_tail(tail_y, tail_x, difference, board)

        break 
        
        
if __name__ == '__main__':
    data = read_data('./data/day_9_test.txt')
    round1(data)