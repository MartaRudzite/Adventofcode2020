import copy

# in_file = 'input_11_test.txt'
in_file = 'input_11.txt'

input_grid = [line.rstrip() for line in open(in_file)]

 # take input grid of seats and turn it into padded seat occupation map
 # 0 - empty seat
 # 1 - occupied seat
 # 2 - floor

seats = []
seats.append([2 for i in range(len(input_grid[0])+2)])

for row in input_grid:
    seats.append([])
    seats[-1].append(2)
    for seat in row:
        if seat == '.':
            seats[-1].append(2)
        elif seat == 'L':
            seats[-1].append(0)
    seats[-1].append(2)

seats.append([2 for i in range(len(input_grid[0])+2)])

# for row in seats:
#     print(row)
# print('')

# __________________________________________________________________

def neighbours(x, y):
    n_neighbours = 0
    if seats[x-1][y-1] == 1:
        n_neighbours += 1
    if seats[x-1][y] == 1:
        n_neighbours += 1
    if seats[x-1][y+1] == 1:
        n_neighbours += 1
    if seats[x][y-1] == 1:
        n_neighbours += 1
    if seats[x][y+1] == 1:
        n_neighbours += 1
    if seats[x+1][y-1] == 1:
        n_neighbours += 1
    if seats[x+1][y] == 1:
        n_neighbours += 1
    if seats[x+1][y+1] == 1:
        n_neighbours += 1
    return n_neighbours

# __________________________________________________________________


while True:
    changes = False
    seats_new = copy.deepcopy(seats)
    for idx, row in enumerate(seats):
        for jdx, seat in enumerate(row):
            if seat == 0:
                if neighbours(idx, jdx) == 0:
                    changes = True
                    seats_new[idx][jdx] = 1
            elif seat == 1:
                if neighbours(idx, jdx) >= 4:
                    changes = True
                    seats_new[idx][jdx] = 0
    seats = copy.deepcopy(seats_new)
    # for row in seats:
    #     print(row)
    # print('')

    if changes == False:
        break


n_1 = 0
for row in  seats:
    for i in row:
        if i == 1:
            n_1 +=1
print(n_1)
