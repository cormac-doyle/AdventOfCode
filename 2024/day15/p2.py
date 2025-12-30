import copy


with open('input.txt') as f:
    data = f.read().strip()

data = data.split('\n')

WIDTH = int(data[0])
BYTES = int(data[1])

BIG_NUMBER = 9999
INVALID_POS = -1
data = data[2:]

matrix = []
for r in range(WIDTH):
    row = []
    for c in range(WIDTH):
        row.append(BIG_NUMBER)
    matrix.append(row)

directions = [
    (0,1),
    (0,-1),
    (-1,0),
    (1,0)
]
valid_range = range(WIDTH)


def dijkstra(matrix):
    steps = 1
    points_tracked = [ (0,0) ]
    matrix[0][0] = 1

    while len(points_tracked) >0:
        next_points = []
        for dr,dc in directions:
            for r,c in points_tracked:
                next_r = r + dr
                next_c = c + dc
                if next_r in valid_range and next_c in valid_range and matrix[next_r][next_c] == BIG_NUMBER:
                    matrix[next_r][next_c] = steps
                    next_points.append( (next_r, next_c) )
    
        steps+=1
    
        points_tracked = next_points
    
    return matrix[WIDTH-1][WIDTH-1] != BIG_NUMBER


for i in range(len(data)):
    points = data[i].split(',')
    row = int(points[1])
    col = int(points[0])
    
    matrix[row][col] = INVALID_POS

    temp_matrix = copy.deepcopy(matrix)
    if dijkstra(temp_matrix) is False:
        # print("Just added point",row,col," and now cant escape")
        break
    # else:
        # print("Found way out in ", temp_matrix[WIDTH-1][WIDTH-1], "steps")

print("Result",(col,row))