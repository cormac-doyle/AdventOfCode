



def check_invalid_p1(id_num):
    id_num= str(id_num)

    half = len(id_num) // 2
    return id_num[0:half] == id_num[half:]



input_ = ''

with open("input.txt") as file:
    input_ = [line.rstrip() for line in file][0]

input_ = input_.split(',')
print(input_)

res = 0

for range_ in input_:

    s = range_.split('-')
    lower = int(s[0])
    upper = int(s[1])

    print(lower, upper)

    for id_to_check in range(lower, upper+1):

        if check_invalid_p1(id_to_check) is True:
            print(id_to_check)
            res+=id_to_check



print('------------')


print(res)

