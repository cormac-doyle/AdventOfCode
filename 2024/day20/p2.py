from copy import deepcopy
from collections import defaultdict


with open('input.txt') as f:
    data = f.read().strip()
data = data.split('\n')

matrix = []
for l in data:
    line = []
    for c in l:
        line.append(c)
    matrix.append(line)

for l in matrix:
    print(l)

matrix_copy = deepcopy(matrix)


directions = [
    (0,1),
    (0,-1),
    (-1,0),
    (1,0)
]

# Find start and end
start = None
end = None

row_range = range(len(matrix))
col_range = range(len(matrix[0]))

for row_idx in row_range:
    for col_idx in col_range:
        if matrix[row_idx][col_idx]=='S':
            start = (row_idx, col_idx)
            continue
        if matrix[row_idx][col_idx] == 'E':
            end = (row_idx, col_idx)


# Start at S and count the length of the racetrack
length =0
race_track = []
curr_pos = start
matrix_copy[curr_pos[0]][curr_pos[1]] = 0
while curr_pos != end:
    race_track.append(curr_pos)
    for d in directions:
        next_pos = (curr_pos[0] +d[0],  curr_pos[1] + d[1] )
         
        if matrix[next_pos[0]][next_pos[1]] == '.' :
            matrix[next_pos[0]][next_pos[1]] = ','
            length+=1
            matrix_copy[next_pos[0]][next_pos[1]] = length
            curr_pos = next_pos
            break
        
        if matrix[next_pos[0]][next_pos[1]] == 'E':
            length+=1
            matrix_copy[next_pos[0]][next_pos[1]] = length
            curr_pos = next_pos

for l in matrix_copy:
    print(l)


print("Length", length)


cheats_map = defaultdict(int)

cheat_directions = [
    (0,2),
    (0,-2),
    (2,0),
    (-2,0)
]

for pos in race_track:
    for d in cheat_directions:
        next_r = pos[0] + d[0]
        next_c = pos[1] + d[1]
        if next_r in row_range and next_c in col_range:
            if matrix_copy[next_r][next_c] != '#':
                # Found a valid race track point
                if matrix_copy[next_r][next_c] > matrix_copy[pos[0]][pos[1]]:
                    time_saved = matrix_copy[next_r][next_c] - matrix_copy[pos[0]][pos[1]] - 2
                    cheats_map[time_saved] +=1


keys = sorted(cheats_map.keys())
# print(keys)

result = 0
for key in keys:
    if key >= 100:
        result+=cheats_map[key]
        # print("There are ", cheats_map[key],"cheats that save ", key, "seconds")

print("Result", result)
