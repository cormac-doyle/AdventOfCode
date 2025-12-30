input_ = []

with open("test.txt") as file:
    input_ = [line.rstrip() for line in file]



'''

brute force approach is easy because we are only checking 2 digits :)

'''


res = 0
for bank in input_:
    max_ = 0

    # brute force
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):

            num_ = int(bank[i] + bank[j])
            # print(i, j, num_)
            max_ = max(max_, num_)

    res+=max_

print(res)