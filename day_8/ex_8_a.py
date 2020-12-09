# in_file = 'input_8_test.txt'
in_file = 'input_8.txt'

lines = [line.rstrip() for line in open(in_file)]
# print(lines)

operations = []
arguments = []
for line in lines:
    a, b = line.split(' ')
    operations.append(a)
    arguments.append(int(b))

# print(operations)
# print(arguments)

repeat = [False for i in range(len(operations))]
i = 0
sum = 0

while True:
    # print(i)
    # print(operations[i])
    # print(lines[i])
    if repeat[i]:
        break
    else:
        repeat[i] = True
        if operations[i] == 'acc':
            sum += arguments[i]
            i += 1
        elif operations[i] == 'jmp':
            i += arguments[i]
        elif operations[i] == 'nop':
            i += 1

print('')
print(sum)
