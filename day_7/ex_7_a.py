in_file = 'input_7_test.txt'
# in_file = 'input_7.txt'

data = [line.rstrip() for line in open(in_file)]

for line in data:
    a, b = line.split('contain')
    aa = a.split(' ')[0]+a.split(' ')[1]
    print(aa)
    print(b)
