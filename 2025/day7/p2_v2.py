
from collections import defaultdict
matrix = None

with open("input.txt") as file:
    matrix = [line.rstrip() for line in file]

'''
.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
'''

beams_count_arr = [0] * len(matrix[0])
'''
beams_map = {
    idx : count of beams
    }
'''

beams_count_arr[matrix[0].find('S')] +=1

i_range = range(len(matrix[0]))

for i in range(1, len(matrix)):
    for beam_idx in range(len(beams_count_arr)):
        if beam_idx >0 and matrix[i][beam_idx] == '^':
            beams_count_arr[beam_idx+1]+=beams_count_arr[beam_idx]
            beams_count_arr[beam_idx-1]+=beams_count_arr[beam_idx]
            beams_count_arr[beam_idx]=0

print(sum(beams_count_arr))
