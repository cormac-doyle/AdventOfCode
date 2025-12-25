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

    print(r)
    print(pos_r,pos_c,vel_r,vel_c)
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

print_matrix(matrix)



def check_tree(matrix):
    left =  0
    right =  WIDTH - 1

    for r in range(HEIGHT-1,-1,-1):
        for c in range(left, right+1):
            if matrix[r][c] != 1:
                print("False",r,c)
                return False
        left+=1
        right-=1
    return True


for pos , vel in p_v:
    pr,pc = pos
    vr,vc = vel

    # print(pr,pc, vr,vc)
    matrix[pr][pc] +=1
    # print_matrix(matrix)
    matrix[pr][pc] -= 1

    new_pr = ( pr + ( vr * SECONDS) ) % HEIGHT
    new_pc = ( pc + ( vc * SECONDS) ) % WIDTH

    matrix[new_pr][new_pc] +=1
    # print(new_pr,new_pc, vr,vc)

print("-"*100)
print_matrix(matrix)

# quadrants:
q_height = ( HEIGHT-1 ) // 2
q_width = ( WIDTH-1 ) // 2



q1, q2, q3, q4 = 0,0,0,0
for r in range(q_height):
    for c in range(q_width):
        q1+= matrix[r][c]
    for c in range(q_width +1,WIDTH): 
        q2+= matrix[r][c]


for r in range(q_height+1, HEIGHT):
    for c in range(q_width):
        q3 += matrix[r][c]
    for c in range(q_width+1,WIDTH):
        q4+= matrix[r][c]
    
    
result =q1*q2*q3*q4
print("Result",result)