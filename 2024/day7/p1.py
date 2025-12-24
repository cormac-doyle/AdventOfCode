

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

for target, ops in operations:
    possibilities = []
    curr = [ops[0]]
    for op in ops[1:]:
        next_ = []
        for val in curr:
            next_.append(val*op)
            next_.append(val+op)

        curr = next_
    
    for val in curr:
        if val == target:
            result+=target
            break


print("Result: ", result)
    
    
