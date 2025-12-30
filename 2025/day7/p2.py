
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

beams_map = defaultdict(int)

'''
beams_map = {
    idx : count of beams
    }
'''

beams_map[matrix[0].find('S')] +=1

i_range = range(len(matrix[0]))

for i in range(1, len(matrix)):
    idxs = list(beams_map.keys())
    for beam_idx in idxs:
        if matrix[i][beam_idx] == '^':
            beams_map[beam_idx+1]+=beams_map[beam_idx]
            beams_map[beam_idx-1]+=beams_map[beam_idx]
            beams_map[beam_idx]=0


print(sum(beams_map.values()))
