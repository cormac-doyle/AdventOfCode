input_ = []

from collections import defaultdict
device_map = defaultdict(list)

with open("input.txt") as file:
    for line in file:
        d1,d_list_str = line.strip().split(':')

        for d in d_list_str.split(' '):
            if d != '':
                device_map[d1].append(d)


for d in device_map:
    print(d, device_map[d])

print('-'*200)
result = [ 0 ]

def dfs(key, curr_path):
    if device_map[key][0] == 'out':
        result[0]+=1
    else:
        for d in device_map[key]:
            next_path = curr_path.copy()
            next_path.append(d)
            dfs(d, next_path)


dfs('you', ['you'])

print('-'*200)
print(result[0])

