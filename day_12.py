import numpy as np 

lets = [chr(i) for i in range(97, 123)]
nums = [i for i in range(1, 27)]
lets.extend(["S", "E"])
nums.extend([0, 27])
SURVEY = dict(zip(lets, nums))

def round1(land):
    scape = np.vectorize(SURVEY.get)(land)
    print(scape)

if __name__ == '__main__':
    data = open('./data/day_12_test.txt', 'r').read()
    data = [[let for let in line] for line in data.split('\n')]
    land = np.array(data, dtype='str')
    
    round1(land)