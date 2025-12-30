input_ = []

'''

811111111111119

434 234234234278


'''

with open("input.txt") as file:
    input_ = [list(line.rstrip()) for line in file]


'''

greedy aproach looking for the local max, for each digit, check the possible indexes, and pick the max num in those possible indexs, if two maxs there, choose the lower index


this approach also works for p1 by making DIGITS equal to 2

'''

DIGITS = 12

res = 0
for bank in input_:
    max_num = []

    start=0
    end = len(bank) - DIGITS
    # print(bank)
    for _ in range(DIGITS):

        local_max = bank[start]
        local_max_index = start
        # print(start, end)
        for i in range(start, end+1):

            if bank[i] > local_max:
                local_max = bank[i]
                local_max_index = i

        # print(local_max)

        max_num.append(str(local_max))
        start = local_max_index + 1
        end += 1

    # print(''.join(max_num))

    max_ = int(''.join(max_num))
    res+=max_

print(res)
