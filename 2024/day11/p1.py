with open('input.txt') as f:
    stones = f.read().strip()

stones = stones.split(" ")
print(stones)

idx = 0
def split_num(new_stones, stone):
    first_ = stone[:len(stone)//2]
    second_ = stone[len(stone)//2:]

    while second_[0]=='0' and len(second_)>1:
        second_ = second_[1:]

    new_stones.append(first_ ) 
    new_stones.append(second_ )

def times2024(new_stones, stone):
    new_stones.append(str(int(stone)*2024))

def add1(new_stones):
    new_stones.append('1')

for _ in range(75):
    new_stones = []
    for stone in stones:
        if stone == '0':
            add1(new_stones)
        elif len(stone)%2==0:
            split_num(new_stones, stone)
        else:
            times2024(new_stones, stone)
    # print(new_stones)
    stones = new_stones
    print(idx, len(stones))
    idx+=1

print("result:",len(stones))

