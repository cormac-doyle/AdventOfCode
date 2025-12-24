from collections import defaultdict

matrix = []

with open('input.txt') as f:
    for l in f:
        matrix.append(l.strip())

# for l in matrix:
#     print(l)

seen = set()

row_range = range(len(matrix))
col_range = range(len(matrix[0]))

directions = [
    (-1,0),
    (1,0),
    (0,1),
    (0,-1),
]

def check_area(curr_char, curr_pos, area_and_perimeter, already_seen, prev_direc, sides_map):
    if curr_pos[0] not in row_range or curr_pos[1] not in col_range or matrix[curr_pos[0]][curr_pos[1]] != curr_char:
        area_and_perimeter[1]+=1
        sides_map[prev_direc].append(curr_pos)
        return
    
    if curr_pos in already_seen:
        return
    
    already_seen.add(curr_pos)
    area_and_perimeter[0]+=1
    
    for dr, dc in directions:
        check_area(curr_char, (curr_pos[0]+dr, curr_pos[1]+dc),area_and_perimeter, already_seen, (dr,dc),sides_map)


def process_sides(sides_map):
    sides = 0

    for dr,dc in sides_map:
        map_by = (0,1)
        if dr == 0:
            map_by = (1,0)
        
        edge_vals_map = defaultdict(list)
        for edges in sides_map[(dr,dc)]:
            edge_vals_map[edges[map_by[0]]].append(edges[map_by[1]])
        
        for k in edge_vals_map:
            edges = sorted(edge_vals_map[k])
            for i in range(len(edges)-1):
                if edges[i+1]-edges[i] !=1:
                    sides+=1
            sides+=1
    return sides


already_covered = set()
result = 0
result2 = 0
for r in row_range:
    for c in col_range:
        a_p = [0,0]
        seen = set()
        sides_map = defaultdict(list)
        if (r,c) not in already_covered:
            check_area(matrix[r][c], (r,c), a_p, seen, (0,0), sides_map)
            already_covered.update(seen)
            # print(matrix[r][c], a_p, a_p[0]*a_p[1])
            result+=a_p[0]*a_p[1]
            sides = process_sides(sides_map)
            # print(matrix[r][c], a_p[0],sides, a_p[0]*sides)
            result2+=a_p[0]*sides

print("Res p1",result)
print("Res p2",result2)
