matrix = []

with open('test.txt') as file:
    for line in file:
        matrix.append(line.strip())

# for l in matrix:
#     print(l)

row_range  = range(len(matrix))
col_range  = range(len(matrix[0]))


directions = [ (0,1), (0,-1), (1,0), (-1,0) ]

    

def dfs(curr_pos, curr_num, already_found):

    if matrix[curr_pos[0]][curr_pos[1]]=='9' and curr_num == 9:
        already_found.add(curr_pos)
        return 1
    unique_paths = 0
    for direc in directions:
        next_pos = (curr_pos[0] + direc[0], curr_pos[1] + direc[1] )
        if next_pos[0]  in row_range and next_pos[1] in col_range and matrix[next_pos[0]][next_pos[1]] == str(curr_num+1):
            unique_paths += dfs(next_pos, curr_num+1, already_found)

    return unique_paths

result_p1 = 0
result_p2 = 0

for row in row_range:
    for col in col_range:
        
        if matrix[row][col] == '0':
            found = set()
            count = dfs((row,col), 0, found)
            # print("From pos", row,col, "found",len(found),'heads and', count,'paths')
            result_p1 += len(found)
            result_p2 += count

print("Result part 1", result_p1)
print("Result part 2", result_p2)
