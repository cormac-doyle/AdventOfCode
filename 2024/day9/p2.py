from collections import defaultdict

with open('input.txt') as f:
    data = f.read().strip()

# data = "2333133121414131402"

# print(data)

id_map = defaultdict(int)

int_list = []

file_lengths = defaultdict(tuple)

disk = ""
id = 0
for i in range(len(data)):
    if i%2==0:
        # disk+= str(id) * int(data[i])
        file_lengths[id] = (len(int_list), int(data[i]))
        for _ in range(int(data[i])):
            int_list.append(id)
        id+=1
    else:
        for _ in range(int(data[i])):
            int_list.append(-1)

id-=1

def print_disk(list):
    new_str = ""
    for num in list:
        if num != -1:
            new_str+=str(num)
        else:
            new_str+='.'
    return new_str

# print(print_disk(int_list))

def find_space_in_disk(int_list, min_space, max_end):

    curr_count = 0
    start_idx = -1
    for i in range(max_end):
        if int_list[i] == -1:
            if curr_count==0:
                start_idx=i
            curr_count+=1
            if curr_count == min_space:
                return start_idx
        else:
            curr_count=0
            start_idx = -1

    return None

def swap_range(arr, start1, start2,length):

    for i in range(length):
        arr[start1] = arr[start2]
        arr[start2] = -1
        start1+=1
        start2+=1

i = 0
for id in range(id, -1, -1):
    start_idx, curr_id_length = file_lengths[id]
    # print("File length for ID", id, start_idx, curr_id_length)
    start_free_space = find_space_in_disk(int_list,curr_id_length,  start_idx)
    if start_free_space is not None:
        # print("Found space at", start_free_space)
        swap_range(int_list, start_free_space, start_idx, curr_id_length)
        # print("Swapped")

    # print(print_disk(int_list))


result = 0
for i in range(len(int_list)):
    if int_list[i]!= -1:
        result+= (i * int_list[i])


# print(print_disk(int_list))
print("Res ", result)