from collections import Counter

# in_file = 'input_6_test.txt'
in_file = 'input_6.txt'

data = [line.rstrip() for line in open(in_file)]

questions = []
count = []

for idx, line in enumerate(data):
    if line != '':
        q = list(line)
        [questions.append(i) for i in q]
    else:
        # print(questions)
        count.append(len(Counter(questions).keys()))
        # count.append(count_unique(questions))
        # print(count[-1])
        questions = []

print(sum(count))
