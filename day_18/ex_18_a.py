in_file = 'input_18.txt'
equations = [line.rstrip('\n') for line in open(in_file)]
# print(data)

sum = 0

# test = '1 + 2 * 3 + 4 * 5 + 6'
# test = '1 + (2 * 3) + (4 * (5 + 6))'
# test = '2 * 3 + (4 * 5)'
# test = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
# test = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
test = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

working_number = [0]
working_action = ['+']
pointer = 0

for i in test:
    if i == ' ':
        continue
    elif i == '+' or i == '-' or i == '*':
        working_action[pointer] = i
    elif i == '(':
        pointer +=1
        working_number.append(0)
        working_action.append('+')
    elif i == ')':
        pointer -=1
        # print('')
        # print(working_number)
        x = working_number.pop()
        # print(working_number)
        # print('')
        # print(working_action)
        action = working_action.pop()
        # print(working_action)
        if working_action[pointer] == '+':
            working_number[pointer] += x
        elif working_action[pointer] == '-':
            working_number[pointer] -= x
        elif working_action[pointer] == '*':
            working_number[pointer] *= x
    else:
        x = int(i)
        if working_action[pointer] == '+':
            working_number[pointer] += x
        elif working_action[pointer] == '-':
            working_number[pointer] -= x
        elif working_action[pointer] == '*':
            working_number[pointer] *= x
        # print(i)
        # print(working_number)

print(working_number[0])
