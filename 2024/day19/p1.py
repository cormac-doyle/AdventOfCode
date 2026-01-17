

from functools import cache


with open('input.txt') as f:
    
    data = f.read().strip()
data = data.split('\n')
print(data)


patterns = set(data[0].split(', '))

stripes = data[2:]


print("patterns", patterns)
print("stripes", stripes)

curr_stripe = None

@cache
def dfs(curr_index):
    result = 0
    if curr_index >= len(curr_stripe):        
        return 1

    for i in range(1, len(curr_stripe) - curr_index + 1):
        if curr_stripe[curr_index : curr_index + i ] in patterns:
            result += dfs( curr_index + i )

    return result


output = 0
for stripe in stripes:
    curr_stripe = stripe
    output+=dfs( 0 )
    dfs.cache_clear()
    

print("Output",output)
