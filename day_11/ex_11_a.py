# in_file = 'input_10_test_1.txt'
# in_file = 'input_10_test_2.txt'
in_file = 'input_10_test.txt'

adapters = [int(line.rstrip()) for line in open(in_file)]

adapters = sorted(adapters)

print(adapters)

delta = [adapters[0],3]

for i in range(len(adapters)-1):
    delta.append(adapters[i+1]-adapters[i])

print(delta)
print(delta.count(1))
print(delta.count(3))
print(delta.count(1)*delta.count(3))
