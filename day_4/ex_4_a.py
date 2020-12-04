in_file = 'input_4.txt'
data = [line.rstrip() for line in open(in_file)]

check_list = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
# print(data[2])
# print(data[3])
n_valid = 0

passport = []
for idx, line in enumerate(data):
    # # if idx+1 == len(data):
    # if idx+1 == 20:
    #     break
    if data[idx] != '':
        item_set = line.split(' ')
        for item in item_set:
            passport.append(item.split(':')[0])
    else:
        # print(passport)
        if len(passport)>=7:
            check = 0
            for i in check_list:
                if i in passport:
                    check += 1
                else:
                    print(idx)
                    print(passport)
                    break
            if check == len(check_list):
                n_valid += 1
                # print(passport)
        passport = []

print(n_valid)
