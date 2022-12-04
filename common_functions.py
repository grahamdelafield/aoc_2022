def read_data(file):
    with open(file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    return data

def chunk_item(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i+3]
