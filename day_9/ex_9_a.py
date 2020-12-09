# in_file = 'input_9_test.txt'
in_file = 'input_9.txt'

# preramble = 5
preramble = 25
lines = [int(line.rstrip()) for line in open(in_file)]

def summing(n):
    sum = []
    for i in range(n, n+preramble):
        for j in range(i+1, n+preramble):
            sum.append(lines[i]+lines[j])
    return sum

# print(summing(0))
sums = summing(0)

for k in range(preramble, len(lines)):
    # print(lines[k])
    # print(sums)
    if lines[k] not in sums:
        print(sums)
        print(lines[k])
        break
    sums = summing(k-preramble+1)
