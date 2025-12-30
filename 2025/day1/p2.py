

input = []

with open("input.txt") as file:
    input = [line.rstrip() for line in file]


'''

Because of the hacky part 1 implementation, part 2 was very easy :)

This would not work for large numbers

'''

curr = 50
res = 0
for line in input:
    direction = line[0]
    amount = int(line[1:])
    operation = 1

    if direction == 'R':
        operation = 1
    else:
        operation = -1

    for i in range(amount):
        curr = curr + operation
        if curr == 100:
            curr = 0

        if curr == -1:
            curr = 99

        if curr == 0:
            res +=1



print(res)
