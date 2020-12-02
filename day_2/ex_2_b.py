in_file = 'input_2.txt'
lines = [line.rstrip('\n') for line in open(in_file)]

# print(lines[1])
result = 0

for line in lines:
    a = line.split(' ')
    min, max = a[0].split('-')
    min = int(min) -1
    max = int(max) -1
    x = a[1][0]
    n = a[2].count(x)
    if (x == a[2][min]) != (x == a[2][max]):
        result += 1

print(result)
