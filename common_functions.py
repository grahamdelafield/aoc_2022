def read_data(file):
    with open(file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    return data