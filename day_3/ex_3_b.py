import numpy as np

in_file = 'input_3.txt'
lines = [line.rstrip('\n') for line in open(in_file)]

length = len(lines[0])
# print(length)

right = [1,3,5,7,1]
down = [1,1,1,1,2]
trees = []

for idx, slope in enumerate(right):
    n_trees = 0
    i = 0
    for line in lines[::down[idx]]:
        if line[i % length] == '#':
            n_trees += 1
        i += slope
    trees.append(n_trees)

# print(np.prod(trees))
# np.prod and math.prod can't cope ;(
out = 1
for i in trees:
    out *= i
print(out)

# print(trees)
