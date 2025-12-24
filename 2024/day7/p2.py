

operations = []
with open('input.txt') as file:
    for line in file:
        val, nums = line.strip().split(':')
        nums = nums.split(' ')
        ints = []
        for num in nums:
            if num != '':
                ints.append(int(num))
        operations.append( (int(val), ints ) )


# for op in operations:
#     print(op)

result = 0

def append_if_valid(arr, val, target):
    if val<= target:
        arr.append(val)


for target, ops in operations:
    possibilities = []
    curr = [ops[0]]
    idx = 0
    for op in ops[1:]:
        next_ = []
        for val in curr:
            append_if_valid(next_,val*op,target)
            append_if_valid(next_,val+op,target)
            append_if_valid(next_, int( str(val)+str(op) ),target)
        curr = next_
    
    for val in curr:
        if val == target:
            result+=target
            break


print("Result: ", result)
    
    
