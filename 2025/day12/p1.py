import copy
from functools import cache

lines = []

with open("test.txt") as file:
    lines=[]
    for l in file:
        lines.append(l.rstrip())
 
def spin(shape):
    new = []
    for i in range(3):
        new_l = ''
        for j in range(2,-1,-1):
            new_l+=shape[j][i]
        new.append(new_l)
    return new

def mirror(shape):
    new = []
    for i in range(2,-1,-1):
        new_l = ''
        for j in range(2,-1,-1):
            new_l+=shape[j][i]
        new.append(new_l)
    return new

def check_shapes_equal(s1,s2):
    for i in range(3):
        for j in range(3):
            if s1[i][j] != s2[i][j]:
                return False
    return True

shapes=[]
idx = 0

for i in range(1,27,5):
    curr_shapes = []
    curr_shape = []
    for l in lines[i:i+3]:
        curr_shape.append(l.replace('#',str(idx)))

    curr_shapes.append(curr_shape)
    for _ in range(3):
        next_ = spin(curr_shape)
        next_flipped = mirror(next_)
        for s in curr_shapes:
            if check_shapes_equal(next_,s):
                break
        else:
            curr_shapes.append(next_)
        curr_shape=next_
    

    idx+=1
    shapes.append(curr_shapes)

print(shapes)

for s_list in shapes:
    print('-'*100)
    for s in s_list:
        for l in s:
            print(l)
        print('-'*100)

print('-'*100)


regions = []

for l in lines[30:]:
    
    area, quantities_str = l.split(':')
    width, height = area.split('x')
    
    quantities = []
    for q in quantities_str.split(' ')[1:]:
        quantities.append(int(q))

    region = (int(width), int(height), quantities)
    regions.append(region)
    print(region)

print('-'*100)

row_range = None
col_range = None


def get_starting_region(width, height):
    region = []
    for _ in range(height):
        line = []
        for _ in range(width):
            line.append('.')
        region.append(line)
    return region

def can_place_shape(curr_region, shape, row, col):
    # print("Checking can place shape")
    for shape_c, c in enumerate(range(col,col+3)):
        for shape_r, r in enumerate(range(row,row+3)):
            if r not in row_range or c not in col_range:
                return False
            if curr_region[r][c] !='.' and shape[shape_r][shape_c] != '.':
                # print("Invalid",r,c,shape_r,shape_c,curr_region[r][c], shape[shape_r][shape_c]  )
                return False
    return True

def place_shape(curr_region, shape, row, col):
    placed = False
    if can_place_shape(curr_region, shape, row, col):
        for shape_c, c in enumerate(range(col,col+3)):
            for shape_r, r in enumerate(range(row,row+3)):
                if shape[shape_r][shape_c] != '.':
                    curr_region[r][c] = shape[shape_r][shape_c]
        return True
    return False
'''

....
....
....
....


'''

def dfs(curr_region, quantities):
    print_matrix(curr_region)
    res = False
    for q in quantities:
        if q > 0:
            break
    else:
        return True

    for i, q in enumerate(quantities):
        if q > 0:
            for r in row_range:
                for c in col_range:
                    for shape in shapes[i]:
                        if can_place_shape(curr_region, shape, r, c):
                            next_region = copy.deepcopy(curr_region)
                            if place_shape(next_region, shape, r, c):
                                next_quantities = quantities.copy()
                                next_quantities[i] -=1
                                res = dfs(next_region, next_quantities)

    return res



def print_matrix(m):
    print('-'*100)
    for l in m:
        print(l)
    print('-'*100)


output = 0
for r in regions:
    width, height, quants = r
    print("quants:",quants)
    row_range = range(height)
    col_range = range(width)

    curr = get_starting_region(width,height)

    if dfs(curr, quants):
        output+=1
    print(output)
    

    # print_matrix(curr)
    # print_matrix(shapes[4][1])

    # place_shape(curr, shapes[4][1], 0 ,0)

    # print_matrix(curr)

    # place_shape(curr, shapes[4][1], 1 ,1)

    # print_matrix(curr)

print(output)
    
