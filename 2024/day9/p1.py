from collections import defaultdict

with open('input.txt') as f:
    data = f.read().strip()

# data = "2333133121414131402"

# print(data)

id_map = defaultdict(int)

int_list = []

disk = ""
id = 0
for i in range(len(data)):
    if i%2==0:
        # disk+= str(id) * int(data[i])
        for _ in range(int(data[i])):
            int_list.append(id)

        id+=1
    else:
        for _ in range(int(data[i])):
            int_list.append(-1)


i = 0
result = 0
while i < len(int_list):
    if int_list[i] == -1:
        int_list[i] = int_list[-1]
        result+= (i*int_list[i])
        del int_list[-1]
        while int_list[-1] == -1:
            del int_list[-1]
    else:
        result+= (i*int_list[i])
    i+=1
# print(int_list)


print("Res ", result)

# id -= 1

# print("Disk", disk)

# id_map_copy = id_map.copy()

# result = 0

# id_start = 0

# curr_id_len = len(str(id))
# i=0
# while i < len(disk):

#     if disk[i:i+curr_id_len] == '.' * curr_id_len:
#         disk = disk[:i] + str(id) + disk[i+curr_id_len:]
#         print("Adding to result", i, id, i*id)
#         result+= (i * id)
#         id_map[id]-=1
#         if id_map[id] == 0:
#             id-=1
            
#         # print("Add",disk)
#         curr_id_len = len(str(id))
#         disk = disk[:-1 * curr_id_len:]
#         while disk[-1] == '.':
#             disk = disk[:-1]
#         # print("Del",disk)
#     elif disk[i:i+len(str(id_start))] == str(id_start):
#         result += (i * id_start)
#         print("Adding to result", i, id_start, i*id_start)
#         id_map[id_start]-=1
#         if id_map[id_start]==0:
#             id_start+=1

#     i+=1


# print("Disk: ",disk)
# print("Result: ", result)
