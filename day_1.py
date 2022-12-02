from common_functions import read_data


def main1():
    data = read_data('./data/day_1.txt')
    
    totals = []

    running = 0
    for entry in data:
        if entry == '':
            totals.append(running)
            running = 0
        if entry != '':
            running += int(entry)

    return max(totals)

def main2():
    data = read_data('./data/day_1.txt')
    
    totals = []

    running = 0
    for entry in data:
        if entry == '':
            totals.append(running)
            running = 0
        if entry != '':
            running += int(entry)
    totals = sorted(totals, reverse=True)

    top3 = totals[:3]
    print(sum(top3))

    return sum(top3)



if __name__ == '__main__':
    result1 = main1()
    print(result1)
    result2 = main2()
    print(result2)