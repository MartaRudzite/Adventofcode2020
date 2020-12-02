in_file = 'input_2.txt'
lines = [line.rstrip('\n') for line in open(in_file)]

# print(lines[1])
result = 0

for line in lines:
    a = line.split(' ')
    min, max = a[0].split('-')
    min = int(min)
    max = int(max)
    x = a[1][0]
    n = a[2].count(x)
    if n >= min and n <= max:
        result += 1

print(result)
