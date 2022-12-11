from common_functions import read_data
import numpy as np
import cProfile


def grab_trees(y, x, forest):
    """Grab all trees to left, right, top and bottom. Order to stem 
    away from root."""
    height = forest[y,x]
    test = forest - height

    up = test[:y,x][::-1]
    down = test[y+1:,x]
    left = test[y,:x][::-1]
    right = test[y,x+1:]

    return up, down, left, right

def round1(data):
    # get shape, add outside trees to count
    y_dim, x_dim = data.shape 
    num_seen = y_dim*2 + (x_dim-2)*2

    # get all trees
    for y in range(1, y_dim-1):
        for x in range(1, x_dim-1):

            up, down, left, right = grab_trees(y, x, data)

            # if any no trees equal or greater, count as seen
            for look in [up, down, left, right]:
                look = look<0
                if look.all():
                    num_seen += 1
                    break
    print(num_seen)
            
def check_line(arr):
    """Return smallest index where of tree equal or greater in height.
    Current tree is height 0."""
    idx = np.where(arr>=0)
    if not np.size(idx):
        # no items, return maximum distance
        return len(arr)
    return np.min(idx)+1

def round2(data):
    y_dim, x_dim = data.shape

    highest = 0
    # grab all trees
    for y in range(1, y_dim-1):
        for x in range(1, x_dim-1):
            
            up, down, left, right = grab_trees(y, x, data)
            
            # find nearest seen tree
            total = 1
            for look in [up, down, left, right]:
                total *= check_line(look)

            # if spot is better than last, keep this one
            highest = np.max(np.array([highest, total]))
            
    print(highest)

      
if __name__ == '__main__':
    data = read_data('./data/day_8.txt')
    data = [[int(d) for d in line] for line in data]
    data = np.array(data)
    round1(data)
    round2(data)

    cProfile.run('round1(data)')
    cProfile.run('round2(data)')