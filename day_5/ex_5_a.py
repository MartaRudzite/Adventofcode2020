in_file = 'input_5.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

def row(x):
    min = 1
    max = 128
    n = 2
    for i in x:
        delta = (128/n) -1
        n= n*2
        if i == 'F':
            max = min + delta
        elif i == 'B':
            min = max - delta
    return min - 1

def col(x):
    min = 1
    max = 8
    n = 2
    for i in x:
        delta = (8/n) -1
        n= n*2
        if i == 'L':
            max = min + delta
        elif i == 'R':
            min = max - delta
        # print(min,' ',max)
    return min - 1

ids = []

for seat in data:
    ids.append((row(seat[:7]) * 8) + col(seat[7:]))

print(int(max(ids)))
