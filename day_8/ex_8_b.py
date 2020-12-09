in_file = 'input_8_test.txt'
# in_file = 'input_8.txt'

lines = [line.rstrip() for line in open(in_file)]
# print(lines)

operations = []
arguments = []
for line in lines:
    a, b = line.split(' ')
    operations.append(a)
    arguments.append(int(b))

ll = len(operations)
print(ll)

def program(operations_i):
    repeat = [False for i in range(ll)]
    i = 0
    sum = 0
    while True:
        print(i)
        if i > ll:
            corrupted = False
            # print('stop')
            break
        elif repeat[i]:
            corrupted = True
            print('stop')
            break
        else:
            repeat[i] = True
            if operations_i[i] == 'acc':
                sum += arguments[i]
                i += 1
            elif operations_i[i] == 'jmp':
                i += arguments[i]
            elif operations_i[i] == 'nop':
                i += 1

    return corrupted, sum

for j in range(ll):
    operations_i = operations
    if operations[j] == 'jmp':
        operations_i[j] = 'nop'
    elif operations[j] == 'nop':
        operations_i[j] = 'jmp'
    else:
        continue
    corrupted, sum = program(operations_i)
    if corrupted == 'False':
        print(sum)
        break
    else:
        print(j)
