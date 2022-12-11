from common_functions import read_data

def make_tree(data):
    data = [d.replace('$ ', '') for d in data]
    records = {}
    tree = []
    for d in data:
        console = d.split(' ')
        match console[0]:
            case 'cd':
                head_dir = console[1]
                if head_dir == '..':
                    this_dir = '/'.join(tree)
                    total_to_add = records.get(this_dir, 0)

                    tree = tree[:-1]
                    this_dir = '/'.join(tree)
                    records[this_dir] = records.get(this_dir, 0) + total_to_add

                else:
                    tree.append(head_dir)
            
                this_dir = '/'.join(tree)

            case 'ls':
                pass 
                
            case 'dir':
                pass 
                
            case other:
                records[this_dir] = records.get(this_dir, 0) + int(console[0])

    while tree != ['/']:
        this_dir = '/'.join(tree)
        total_to_add = records.get(this_dir, 0)
        
        tree = tree[:-1]
        this_dir = '/'.join(tree)
        records[this_dir] = records.get(this_dir, 0) + total_to_add

    return records

        
def get_sum_valid(tree):
    ans = sum([v for v in tree.values() if v <= 100_000])
    print(ans)

def find_smallest_valid(tree):
    total = 70000000
    used = tree['/']

    needed = 30000000 - (total - used) 
    ans = min([v for v in tree.values() if v >= needed])
    print(ans)

if __name__ == '__main__':
    data = read_data('./data/day_7.txt')
    tree = make_tree(data)
    s = get_sum_valid(tree)
    m = find_smallest_valid(tree)
