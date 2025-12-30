
input_ = None

with open("input.txt") as file:
    input_ = [line.rstrip() for line in file]


# print(input_)
ranges = []

idx = 0
for line in input_:
    idx+=1
    if line == '':
        break
    line = line.split('-')
    lower = int(line[0])
    upper = int(line[1])

    ranges.append([lower, upper])


result = 0

for i in range(idx, len(input_)):

    num_to_check = int(input_[i])

    for r in ranges:
        if num_to_check >= r[0] and num_to_check <= r[1]:
            result+=1
            break

print( result )
