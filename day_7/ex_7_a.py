in_file = 'input_7_test.txt'
# in_file = 'input_7.txt'

data = [line.rstrip() for line in open(in_file)]

# contain = []
up = {}

for line in data:
    a, b = line.split('contain')
    if 'no other bags' in b:
        continue
    aa = a.split(' ')[0]+a.split(' ')[1]
    b = b.split(',')
    for i in b:
        # print(i.split(' '))
        bb = i.split(' ')[2]+i.split(' ')[3]
        if bb in up:
            up[bb].append(aa)
        else:
            up[bb] = [aa]
# print(up)

queue = ['shinygold']
outerbag = []

while queue:
    print(queue)
    x = queue.pop(0)
    if x in up:
        for i in up[x]:
            if (i not in queue) and (i not in outerbag):
                queue.append(i)
    else:
        outerbag.append(x)

print(outerbag)
print(len(outerbag))
