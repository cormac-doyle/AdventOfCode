

def check_invalid_p2(id_num):
    id_num = str(id_num)

    # cool one liner trick i found online
    # return id_num in (id_num+id_num)[1:-1]

    # this was my initial implementation
    # print(id_num)

    for i in range(1, (len(id_num)//2) + 1):

        temp = id_num[0:i]
        # print("Checking blocks ", i)
        
        for j in range(i, len(id_num), i):
            # print(temp,  id_num[j:j+i])
            if temp != id_num[j:j+i]:
                break

            temp = id_num[j:j+i]
        else:
            return True

    return False


def check_invalid_p1(id_num):
    id_num= str(id_num)

    half = len(id_num) // 2
    return id_num[0:half] == id_num[half:]


'''

1188511880-1188511890

46452718-46482242


'''

input_ = ''

with open("input.txt") as file:
    input_ = [line.rstrip() for line in file][0]

input_ = input_.split(',')
# print(input_)


from datetime import datetime
start_time = datetime.now()
res = 0

for range_ in input_:

    s = range_.split('-')
    lower = int(s[0])
    upper = int(s[1])

    # print(lower, upper)

    for id_to_check in range(lower, upper+1):

        if check_invalid_p2(id_to_check) is True:
            # print(id_to_check)
            res+=id_to_check



print('------------')


print(res)

end_time = datetime.now()
time_take = end_time-start_time
print("Time take: ", time_take)