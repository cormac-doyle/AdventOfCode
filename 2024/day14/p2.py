
robots = []

HEIGHT = 103
WIDTH = 101

SECONDS = 100

with open('input.txt') as f:
    robots = f.read().strip()

robots = robots.split('\n')


p_v = []
for r in robots:
    parts = r.split(' ')
    pos = parts[0][2:]
    pos=pos.split(',')
    pos_r, pos_c = int(pos[1]), int(pos[0])

    vel = parts[1][2:]
    vel=vel.split(',')
    vel_r, vel_c = int(vel[1]), int(vel[0])

    # print(r)
    # print(pos_r,pos_c,vel_r,vel_c)
    p_v.append( [ [pos_r,pos_c] , (vel_r, vel_c) ] )


matrix = []
for _ in range(HEIGHT):
    row = []
    for _ in range(WIDTH):
        row.append(0)
    matrix.append(row)


def print_matrix(matrix):
    for l in matrix:
        print(l)

# print_matrix(matrix)

def check_tree(matrix):
    left =  0
    right =  WIDTH - 1

    for r in range(HEIGHT-1,-1,-1):
        
        if matrix[r][left] != 1 or matrix[r][right] != 1:
            # print("False",r,c)
            return False
        left+=1
        right-=1
    return True
import copy
clean_matrix = copy.deepcopy(matrix)
print("-"*100)
print_matrix(clean_matrix)
print("-"*100)
SECONDS = 1

seconds = 0

while True:
    matrix = copy.deepcopy(clean_matrix)
    # print("Clean:")
    # print_matrix(matrix)
    # print("-"*100)
    for i in range(len(p_v)):
        pr,pc = p_v[i][0]
        vr,vc = p_v[i][1]

        # print(pr,pc, vr,vc)
        # matrix[pr][pc] +=1
        # print_matrix(matrix)
        # matrix[pr][pc] -= 1

        new_pr = ( pr + ( vr * SECONDS) ) % HEIGHT
        new_pc = ( pc + ( vc * SECONDS) ) % WIDTH
        p_v[i][0] = [new_pr, new_pc]
        matrix[new_pr][new_pc] +=1
        # print(new_pr,new_pc, vr,vc)
    print_matrix(matrix)
    print("-"*100)
    seconds+=1
    if check_tree(matrix):
        print("Christmas tree found after ",seconds, "seconds")
        break
    print(seconds)

    
    

# print("-"*100)
# print_matrix(matrix)





