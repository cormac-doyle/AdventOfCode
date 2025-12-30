
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

ranges.sort()
print(ranges)

inc = 1
i = 0
while i < len(ranges)-1:
    
    #print(ranges[i],ranges[i+1] , ranges)
    if ranges[i][1] >= ranges[i+inc][0] and ranges[i][1] < ranges[i+inc][1]:
        ranges[i][1] = ranges[i+inc][1]
        #print('Merging upper')
        inc+=1

    elif ranges[i][1] >= ranges[i+inc][0] and ranges[i][1] >= ranges[i+inc][1]:
        #print('Deleting next range')
        inc+=1

    else:
        result+= (ranges[i][1]-ranges[i][0]+1)
        i = i + inc
        inc=1

result += (ranges[-1][1]-ranges[-1][0]+1)

print(ranges)

print('---------------------------')
print(result)
