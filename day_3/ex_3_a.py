in_file = 'input_3.txt'
lines = [line.rstrip('\n') for line in open(in_file)]

lenght = len(lines[0])
# print(lenght)

n_trees = 0
i = 0

for line in lines:
    if line[i % lenght] == '#':
        n_trees += 1
    i += 3

print(n_trees)
