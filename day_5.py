from common_functions import read_data
import re
import cProfile

def split_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    i = 0
    while data[i] != '\n':
        i += 1
    board = data[:i]
    moves = data[i+1:]

    # get max number from index row
    shape = max([int(i) for i in re.findall('\d+', data[i-1])])

    return shape, board, moves

def make_board(board, shape=3):
    containers = []

    # iterate through board backwards
    for l in board[:-1]:
        containers.extend(l[1::4])
    
    # divide into columns
    refreshed = [containers[i::shape] for i in range(shape)]

    # replace all empty spaces
    for i, r in enumerate(refreshed):
        refreshed[i] = [let for let in ''.join(r).strip().replace(' ','')]

    return refreshed
        
def round1(data, board, reverse=True):
    for d in data:
        # find what to do
        num, start, end = [int(i)-1 for i in re.findall('\d+', d)]

        # add 1 to number of containers because its an amount, not index
        num += 1
        moved = board[start][:num]

        # if cratemoover 9000, reverse list
        if reverse:
            moved = moved[::-1]

        # fix piles
        board[end] = moved + board[end]
        board[start] = board[start][num:]
    
    print(''.join([c[0] for c in board]))

if __name__ == '__main__':
    shape, master_board, moves = split_data('./data/day_5.txt')

    board = make_board(master_board, shape=shape)
    round1(moves, board)
    cProfile.run('round1(moves, board)')

    board = make_board(master_board, shape=shape)
    round1(moves, board, reverse=False)
    cProfile.run('round1(moves, board, reverse=False)')