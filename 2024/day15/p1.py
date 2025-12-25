


with open('input.txt') as f:
    data = f.read().strip()

data = data.split('\n')

WIDTH = int(data[0])
BYTES = int(data[1])
data = data[2:]

matrix = []
for r in range(WIDTH):
    row = []
    for c in range(WIDTH):
        row.append(9999)
    matrix.append(row)


for i in range(BYTES):
    points = data[i].split(',')
    row = int(points[1])
    col = int(points[0])
    print(row,col)
    matrix[row][col] = '#'

for l in matrix:
    print(l)

directions = [
    (0,1),
    (0,-1),
    (-1,0),
    (1,0)
]
valid_range = range(WIDTH)


steps = 1
points_tracked = [ (0,0) ]
matrix[0][0] = 1

print( '-' * 100 )

while len(points_tracked) >0:
    next_points = []
    for dr,dc in directions:

        for r,c in points_tracked:
            next_r = r + dr
            next_c = c + dc
            if next_r in valid_range and next_c in valid_range and matrix[next_r][next_c] != '#' and matrix[next_r][next_c] > steps:
                matrix[next_r][next_c] = steps
                next_points.append( (next_r, next_c) )
    
    steps+=1
    
    points_tracked = next_points
    

print("Result", matrix[WIDTH-1][WIDTH-1])
