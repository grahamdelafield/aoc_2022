from common_functions import read_data
import cProfile

vals = [i for i in range(1, 4)]

# rock, paper, scissors
play1 = ["A", "B", "C"]
play2 = ["X", "Y", "Z"]

his_plays = dict(zip(play1, vals))
my_plays = dict(zip(play2, vals))

def round1():    
    # win, loss, draw
    results = {-2:6, 1:6, -1:0, 2:0, 0:3}

    data = read_data('./data/day_2.txt')

    totals = []
    for round in data:
        his, my = round.split(' ')
        res = my_plays[my] - his_plays[his]

        round_val = results[res]
        round_sum = round_val + my_plays[my]
        
        totals.append(round_sum)

    return sum(totals)


def round2():
    data = read_data('./data/day_2.txt')

    results = {"X":0, "Y":3, "Z":6}

    totals = []
    for round in data:
        his, my = round.split(' ')

        match my:
            case "X":
                my_val = play1[play1.index(his)-1]
                round_val = results[my] + his_plays[my_val]
            case "Y":
                round_val = results[my] + his_plays[his]
            case "Z":
                my_val = play1[play1.index(his)+1 - 3]
                round_val = results[my] + his_plays[my_val]
        totals.append(round_val)
    return sum(totals)

if __name__ == '__main__':
    print(cProfile.run('round1()'))
    result1 = round1()
    print(result1)
    print(cProfile.run('round2()'))
    result2 = round2()
    print(result2)

