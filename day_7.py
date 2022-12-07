from common_functions import read_data
import re
import json

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def make_tree(data):
    records = {}
    data = [d.replace('$ ', '') for d in data]
    tree = []
    for d in data:
        console = d.split(' ')
        match console[0]:
            case 'cd':
                head_dir = console[1]
                if head_dir == '..':
                    head_dir = tree.pop(-1)
                    continue

                else:
                    tree.append(head_dir)
                print(tree)

                new = {head_dir:{'files':[],'dirs':[]}}
                current = records.get(head_dir, new)
            
            case 'ls':
                pass 
            
            case 'dir':
                print(current, head_dir)
                current[head_dir]['dirs'].append(console[1])
            
            case other:
                current[head_dir]['files'].append(int(console[0]))
        
        records.update(current)
    
    return records

def get_sum(tree, dir):
    these_contents = tree[dir]

    # get immediate contents
    this_val = sum(these_contents['files'])

    # recurse to get subcontents
    sub_vals = sum([get_sum(tree, d) for d in these_contents['dirs']]) 
    
    return  this_val + sub_vals


def get_totals(tree, max_size=100_000):
    totals = []
    for head, rec in tree.items():
        print(f'{head} contains {rec["dirs"]}')
        val = sum(rec['files']) + sum([get_sum(tree, d) for d in rec['dirs']])
        print(head, val)
        if val <= max_size:
            totals.append(val)
    print(sum(totals))
        
    

if __name__ == '__main__':
    data = read_data('./data/day_7.txt')
    tree = make_tree(data)
    print(tree)
    get_totals(tree)

