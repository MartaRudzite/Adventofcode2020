# in_file = 'input_13_test.txt'
in_file = 'input_13.txt'

time, bus_ids = [line.rstrip() for line in open(in_file)]

time = int(time)
bus_ids = bus_ids.split(',')

# print(time)
# print(bus_ids)

bus_list = []
bus_list_times = []

for bus in bus_ids:
    if bus == 'x':
        continue
    id = int(bus)
    # print(id)
    bus_list.append(id)
    bus_time = 0
    while bus_time < time:
        bus_time += id
    bus_list_times.append(bus_time - time)

min_wait = min(bus_list_times)

# print(bus_list_times)
# print(min_wait)

idx = bus_list_times.index(min_wait)

# print(bus_list[idx])

print(min_wait*bus_list[idx])
