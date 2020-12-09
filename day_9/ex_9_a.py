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
        # print(sums)
        # print(lines[k])
        key = lines[k]
        break
    sums = summing(k-preramble+1)

# ------------------------------------------
min_i = 0
max_i = 2
# print(sum(lines[min:max]))
while True:
    total = sum(lines[min_i:max_i])
    if total == key:
        print(sum(lines[min_i:max_i]))
        print(lines[min_i:max_i])
        print(min(lines[min_i:max_i])+max(lines[min_i:max_i]))
        break
    elif total < key:
        max_i +=1
    elif total > key:
        min_i +=1
