input_ = []


with open("input.txt") as file:
    input_ = [list(line.rstrip()) for line in file]

def check_point(i, j, matrix, i_range,j_range):
    
    if i in i_range and j in j_range and matrix[i][j] == '@':
        return 1
    return 0

def check_around(i, j, matrix, i_range,j_range):
    rolls = 0

    rolls += check_point(i+1,j,matrix, i_range,j_range )
    rolls += check_point(i-1,j,matrix, i_range,j_range )
    rolls += check_point(i+1,j+1,matrix, i_range,j_range )
    rolls += check_point(i+1,j-1,matrix, i_range,j_range )
    rolls += check_point(i-1,j+1,matrix, i_range,j_range )
    rolls += check_point(i-1,j-1,matrix, i_range,j_range )
    rolls += check_point(i,j+1,matrix, i_range,j_range )
    rolls += check_point(i,j-1,matrix, i_range,j_range )

    return rolls


j_max = len(input_)
i_max = len(input_[0])

j_range = range(j_max)
i_range = range(i_max)

res = 0

for j in j_range:
    for i in i_range:
        if input_[i][j] == '@':
            surrounding = check_around(i, j, input_, i_range, j_range)

            if  surrounding < 4:
                res+=1



print('-------------------------------------------------')
print(res)
