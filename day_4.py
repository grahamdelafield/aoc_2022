from common_functions import read_data
import cProfile

DATA = read_data('./data/day_4.txt')

def split_cast(line):
    left, right = line.split(',')

    # get all things between start and end
    left_s, left_e = [int(s) for s in left.split('-')]
    left = [l for l in range(left_s, left_e+1)]
    left = set(left)
    
    right_s, right_e = [int(s) for s in right.split('-')]
    right = [l for l in range(right_s, right_e+1)]
    right = set(right)

    return left, right


def round1(data):
    encaps = 0
    for d in data:
        left, right = split_cast(d)

        # find if one is within other
        if left.issuperset(right) or right.issuperset(left):
            encaps += 1
    
    print(encaps)


def round2(data):
    encaps = 0
    for d in data:
       left, right = split_cast(d)
       
       # find if unique length is lower than total length
       if len(left.union(right))<len(left)+len(right):
            encaps += 1

    print(encaps)

        
if __name__ == '__main__':
    round1(DATA)
    round2(DATA)
    cProfile.run('round1(DATA)')
    cProfile.run('round2(DATA)')