# my_ticket = [89,139,79,151,97,67,71,53,59,149,127,131,103,109,137,73,101,83,61,107]

in_file = 'input_rules.txt'
# in_file = 'input_rules_test.txt'
rules_in = [line.rstrip('\n') for line in open(in_file)]

in_file = 'input_16.txt'
# in_file = 'input_16_test.txt'
tickets = [line.rstrip('\n') for line in open(in_file)]

valid_range = []

for line in rules_in:
    ranges = line.split(':')[1].split(' ')
    range_1 = ranges[1].split('-')
    range_2 = ranges[3].split('-')
    set = [i for i in range(int(range_1[0]),int(range_1[1])+1)]
    valid_range += set
    set = [i for i in range(int(range_2[0]),int(range_2[1])+1)]
    valid_range += set

print(valid_range)
ticket_error_rate = 0

for ticket in tickets:
    val = ticket.split(',')
    for i in val:
        if int(i) not in valid_range:
            ticket_error_rate += int(i)
            print(i)
            break



print('')
print(ticket_error_rate)
