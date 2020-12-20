# in_file = 'input_12_test.txt'
in_file = 'input_12.txt'

actions = [line.rstrip() for line in open(in_file)]

x = 0
y = 0

x_w = 10
y_w = 1
direction = 'E'

for i in actions:
    action = i[0]
    val = int(i[1:])
    # print(action,' ',val)
    if action == 'N':
        y_w += val
    elif action == 'S':
        y_w -= val
    elif action == 'E':
        x_w += val
    elif action == 'W':
        x_w -= val
    elif action == 'F':
        x += x_w * val
        y += y_w * val
    elif action == 'L':
        n_turn = int(val /90)
        for j in range(n_turn):
            hold = x_w
            x_w = -y_w
            y_w = hold
    elif action == 'R':
        n_turn = int(val /90)
        for j in range(n_turn):
            hold = x_w
            x_w = y_w
            y_w = -hold
    # print(x,' ',y)
    # print(x_w,' ',y_w)

print(abs(x)+abs(y))
