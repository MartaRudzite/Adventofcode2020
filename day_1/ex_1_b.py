in_file = 'input_1.txt'
data = [line.rstrip('\n') for line in open(in_file)]
# print(data)

data = [int(i) for i in data]

for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]+data[j]<2020:
            for k in range(j+1,len(data)):
                if data[i]+data[j]+data[k]==2020:
                    print(data[i]*data[j]*data[k])
