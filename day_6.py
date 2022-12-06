from common_functions import read_data
import cProfile

DATA = read_data('./data/day_6.txt')

def parse(data, window_size):
    # parse each line (only for tests)
    for d in data:
        i = 0

        # grab packet
        window = d[i:i+window_size]
        
        # slide window until packet length == number unique chars, exit
        while len(window) != len(set(window)):
            i += 1
            window = d[i:i+window_size]
        print(f'packet found at {i+window_size}')


if __name__ == '__main__':
    parse(DATA, 4)
    parse(DATA, 14)

    cProfile.run('parse(DATA, 4)')
    cProfile.run('parse(DATA, 14)')