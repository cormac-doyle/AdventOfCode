with open('input.txt') as f:
    stones = f.read().strip()

stones = stones.split(" ")
print(stones)

ints = []
for s in stones:
    ints.append(int(s))
stones = ints

idx = 0

def has_even_digits(n):
    if n == 0: return False
    n = abs(n)
    
    count = 0
    while n > 0:
        n //= 10
        count += 1
        
    return count % 2 == 0

import math

def split_number(n):
    if n == 0:
        return 0, 0
    
    # 1. Get total number of digits
    digit_count = int(math.log10(abs(n))) + 1
    
    # 2. Find the power of 10 that represents the halfway point
    # For 4 digits, we need 10^2 (100). For 6 digits, 10^3 (1000).
    mid = digit_count // 2
    divisor = 10**mid
    
    # 3. Use math operators to split
    left = n // divisor
    right = n % divisor
    
    return left, right  

for _ in range(75):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif has_even_digits(stone):
            left, right = split_number(stone)
            new_stones.append(left)
            new_stones.append(right)

        else:
            new_stones.append(stone*2024)
    # print(new_stones)
    stones = new_stones
    print(idx, len(stones))
    idx+=1

print("result:",len(stones))

