with open('test.txt') as f:
    data = f.read().strip()

data = data.split('\n')
matrix = []
for l in data:
    row = []
    for char in l:
        if char != '#':
            row.append(99999999)
        else:
            row.append(char)
            
    matrix.append(row)
    

row_range = range(1, len(matrix)-1)
col_range = range(1, len(matrix[0])-1)

tracked_points = set()
tracked_points.add( (len(matrix)-2, 1, 0, 1 ))

directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]
matrix[len(matrix)-2][1] = 0

def print_matrix():
    for l in matrix:
        row_to_print = []
        for char in l:
            if char == 99999999:
                row_to_print.append('.')
            else:
                row_to_print.append(char)
        print(row_to_print)
    print('-'*100)

while len(tracked_points) > 0:
    print(len(tracked_points))
    print_matrix()
    next_points = set()
    for r, c, curr_r_dir, curr_c_dir in tracked_points:
        for dr , dc in directions:
            if (r + dr) in row_range and (c + dc) in col_range:
                if matrix[r + dr][c + dc] != '#':
                    next_score = matrix[r][c] + 1
                    if (curr_r_dir, curr_c_dir) != ( dr, dc ):
                        next_score+=1000
                    if next_score < matrix[r + dr][c + dc]:
                        matrix[r + dr][c + dc] = next_score
                        next_points.add( (r + dr, c + dc, dr , dc) )

    tracked_points = next_points


for l in matrix:
    print(l)

print("Result", matrix[1][len(matrix[0])-2])

