from common_functions import read_data, chunk_item

DATA = read_data('./data/day_3.txt')

# create map from disordered ascii
lets = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
nums = [i for i in range(1, len(lets)+1)]
LOOK = dict(zip(lets, nums))

def round1(data):
    priors = []
    for sack in data:
        # divide sack
        middle = len(sack)//2
        left, right = sack[:middle], sack[middle:]

        # determine uniqe chars
        left, right = set(left), set(right)

        # see what chars in both
        share = left&right
        
        # get value
        priors.extend([LOOK[i] for i in share])
    
    print(sum(priors))


def check_bags(bags):
    """Iterate through bags and keep only common letters"""
    s = set(bags[0])
    for b in bags[1:]:
        s = s&set(b)
    return s

def chunk_item(data: list, size: int):
    """Divide iterator into even parts"""
    for i in range(0, len(data), size):
        yield data[i:i+3]


def round2(data):
    # get groups of three
    chunks = [c for c in chunk_item(data, 3)]
    
    totals = []
    for c in chunks:
        # check each bag
        badge = check_bags(c)

        # add total 
        totals.extend([LOOK[i] for i in badge])

    print(sum(totals))


if __name__ == '__main__':
    round1(DATA)
    round2(DATA)