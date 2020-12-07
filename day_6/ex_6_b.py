from collections import Counter

# in_file = 'input_6_test.txt'
in_file = 'input_6.txt'

data = [line.rstrip() for line in open(in_file)]

questions = []
count = []
n = 0

for line in data:
    if line != '':
        q = list(line)
        if n == 0:
            [questions.append(i) for i in q]
        else:
            qq = []
            for i in q:
                if i in questions:
                    qq.append(i)
            questions = qq
        n += 1
    else:
        count.append(len(questions))
        questions = []
        n = 0

print(sum(count))
