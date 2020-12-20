# numbers = [3,0]                     # 436
# next = 6
numbers = [1,20,13,6,12,0]         # puzzle input
next = 17



while len(numbers) <2020:
    try:
        i = numbers.index(next) +1
    except ValueError:
        i = 0
    numbers.insert(0,next)
    next = i
    # print(numbers)

print(numbers[0])
