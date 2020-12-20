# in_file = 'input_12_test.txt'
in_file = 'input_12.txt'

actions = [line.rstrip() for line in open(in_file)]

turn_R = ['N','E','S','W','N','E','S','W']
turn_L = ['N','W','S','E','N','W','S','E']

x = 0
y = 0
direction = 'E'

for i in actions:
    action = i[0]
    val = int(i[1:])
    # print(action,' ',val)
    if action == 'N':
        y += val
    elif action == 'S':
        y -= val
    elif action == 'E':
        x += val
    elif action == 'W':
        x -= val
    elif action == 'F':
        if direction == 'N':
            y += val
        elif direction == 'S':
            y -= val
        elif direction == 'E':
            x += val
        elif direction == 'W':
            x -= val
    elif action == 'L':
        n_turn = int(val /90)
        idx = turn_L.index(direction)
        direction = turn_L[idx+n_turn]
    elif action == 'R':
        n_turn = int(val /90)
        idx = turn_R.index(direction)
        direction = turn_R[idx+n_turn]
    # print(x,' ',y)

print(abs(x)+abs(y))
