

input = []

with open("input.txt") as file:
    input = [line.rstrip() for line in file]


'''

This is a bit of ahck and only works because the numbers are quite small (this is not high performant solution)

Turned out to make part 2 a lot easier :)

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
