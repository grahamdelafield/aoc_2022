from common_functions import read_data, chunk_item
import numpy as np
import matplotlib.pyplot as plt

def get_values(data):
    values = []
    for d in data:
        match d[:4]:
            case 'addx':
                values.extend([0, int(d[5:])])
            case 'noop':
                values.append(0)
    
    # inital value is 1
    values[0] = 1

    # cumulative sum
    return np.cumsum(np.array(values))

def round1(arr):
    # get positions
    idx = np.linspace(20, 220, 6, dtype=int)

    # multiple indexed positions by round number
    print(np.cumsum(arr[idx-2] * idx))

def round2(arr):
    
    running = []

    # make start line
    sprite = ['#', '#', '#']
    line = ['.']*40
    line[:3]=sprite

    for position, val in enumerate(arr):

        running.append(line[position%40])

        # make new line
        line = ['.']*40
        # place middle of sprite
        line[val-1:val+2] = sprite

        # if too long, wrap (unsure if needed, mine looks better this way)
        line, rem = line[:40], line[40:]
        line[:len(rem)] = rem

    chunks = chunk_item(running, 40)

    for chunk in chunks:
        print(''.join(chunk))

    grid = np.array([1 if p=='#' else 0 for p in running]).reshape(6, 40)
    plt.imshow(grid)
    plt.show()
    


if __name__ == '__main__':
    data = read_data('./data/day_10.txt')
    values = get_values(data)
    round1(values)
    round2(values)