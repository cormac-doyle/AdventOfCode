input_ = []

with open("input.txt") as file:
    input_ = [list(line.rstrip()) for line in file]

surrounding_points = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]



ROLL = '@'

def check_point(i, j, matrix, i_range,j_range):
    if i in i_range and j in j_range and matrix[j][i] == ROLL:
        return 1
    return 0

def count_surrounding(i, j, matrix, i_range, j_range, surrounding_points):
    rolls = 0
    for j_op, i_op in surrounding_points:
        rolls += check_point(i + i_op, j + j_op, matrix, i_range, j_range )

    return rolls


j_max = len(input_)
i_max = len(input_[0])

j_range = range(j_max)
i_range = range(i_max)

res = 0


points_to_check = []
for j in j_range:
    for i in i_range:
        points_to_check.append([j,i])


while True:
    rolls_to_remove = []
    curr_rolls = []
    for j, i in points_to_check:
            if input_[j][i] == ROLL:
                surrounding = count_surrounding(i, j, input_, i_range, j_range, surrounding_points)

                if surrounding < 4:
                    res+=1
                    rolls_to_remove.append([j, i])
                else:
                    curr_rolls.append([j, i])


    if len(rolls_to_remove) == 0:
        break

    for j, i in rolls_to_remove:
        input_[j][i] = '.'

    
    points_to_check = curr_rolls



print('---------------------------------------------------------------------------------')
print( res )
