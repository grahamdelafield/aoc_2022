import re

def dump_barrel(file):
    with open(file, 'r') as f:
        text = f.read()
    text = text.split('\n\n')
    monkeys = [re.split(r'\n+\s+', m) for m in text]
    return monkeys

def study_monkeys(monkeys):
    res = {}
    for m in monkeys:
        for i, component, in enumerate(m):
            match i:
                case 0:
                    ident = re.search(r'\d+', component).group()
                    ident = int(ident)
                case 1:
                    items = re.findall(r'\d+', component)
                    items = [int(i) for i in items]
                case 2:
                    op, val = re.search(r'([\+\-\*\\]+)\s(\w*)', component).groups()
                    if val == 'old':
                        op = '**'
                    else:
                        val = int(val)
                case 3:
                    test = re.search(r'\d+', component).group()
                    test = int(test)
                case 4:
                    true_dest = re.search(r'\d+', component).group()
                    true_dest = int(true_dest)
                case 5:
                    false_dest = re.search(r'\d+', component).group()
                    false_dest = int(false_dest)
        res[ident] = {
            'items':items,
            'operation':op,
            'op_val':val,
            'test':test,
            True:true_dest,
            False:false_dest,
            'ex_count':0
        }
    return res

def throw_round1(journal):
    for i in range(20):
        for notes in journal.values():
            for i in range(len(notes['items'])):
                notes['ex_count'] += 1
                worry = notes['items'].pop(0)
                match notes['operation']:
                    case '*':
                        worry *= notes['op_val']
                    case '\\':
                        worry /= notes['op_val']
                    case '+':
                        worry += notes['op_val']
                    case '-':
                        worry -= notes['op_val']
                    case '**':
                        worry *= worry
                worry = worry // 3
                new_monkey = (
                    notes[worry%notes['test']==0]
                )
                journal[new_monkey]['items'].append(worry)

    counts = [(k, v['ex_count']) for (k, v) in journal.items()]
    counts = sorted(counts, key=lambda x: x[1], reverse=True)
    print(counts[0][1]*counts[1][1])
    return journal


if __name__ == '__main__':
    monkeys = dump_barrel('./data/day_11.txt')
    journal = study_monkeys(monkeys)