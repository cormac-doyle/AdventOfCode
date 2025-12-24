

matrix = []
with open('input.txt') as file:

    for line in file:
        matrix.append(list(line.strip()))


row_range = range(len(matrix))
col_range = range(len(matrix[0]))

for row in row_range:
    # print(matrix[row])
    for col in col_range:
        if matrix[row][col] == '^':
            start_pos = (row, col)
            matrix[row][col] = '.'

def print_matrix(matrix):
    for r in row_range:
        print(matrix[r])
    print("-"*100)

directions = [ (-1,0), (0,1), (1,0), (0,-1)]

def find_path_out(matrix, row_range, col_range, start_pos, directions):
    distinct_pos = set()
    distinct_pos_and_direc = set()
    escaped = False
    curr_pos = start_pos
    curr_direc_idx = 0
    curr_direc = directions[curr_direc_idx]
    while True:

        if (curr_pos, curr_direc_idx) in distinct_pos_and_direc:
            # print("In a loop")
            break

        distinct_pos_and_direc.add( (curr_pos, curr_direc_idx) )
        distinct_pos.add(curr_pos)

        next_pos = (curr_pos[0] + directions[curr_direc_idx][0] , curr_pos[1] + directions[curr_direc_idx][1])

        if next_pos[0] not in row_range or next_pos[1] not in col_range:
        # we are out of bounds and escaped
            # print('Escaped')
            escaped = True
            # matrix[curr_pos[0]][curr_pos[1]] = '.'
            break
        elif matrix[next_pos[0]][next_pos[1]] == '#':
        # apply direction here
            # print("Changing direction")
            curr_direc_idx+=1
            if curr_direc_idx == 4:
                curr_direc_idx=0
        else :
            # matrix[curr_pos[0]][curr_pos[1]] = '.'
            # matrix[next_pos[0]][next_pos[1]] = '^'
            # print_matrix(matrix)
            curr_pos = next_pos
    
    return distinct_pos, escaped


distinct_pos, escaped = find_path_out(matrix, row_range, col_range, start_pos, directions)
        # print_matrix(matrix)

count_ = 0    
for pos in distinct_pos:
    # print("Checking pos:",pos)
    matrix[pos[0]][pos[1]] = '#'
    # print_matrix(matrix)
    _, escaped = find_path_out(matrix, row_range, col_range, start_pos, directions)
    matrix[pos[0]][pos[1]] = '.'
    if escaped == False:
        count_+=1
    # print("-"*100)

print("Result Part 1: ", len(distinct_pos))
print("Result Part 2: ", count_)


    