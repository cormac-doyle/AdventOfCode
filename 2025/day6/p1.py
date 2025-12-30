matrix = None

with open("input.txt") as file:
    matrix = []
    for line in file:
        curr_line = []
        for element in line.rstrip().split(' '):
            if element != '':
                curr_line.append(element)
        matrix.append(curr_line)
    
print(matrix)


row_max = len(matrix)
col_max = len(matrix[0])

result = 0
for col in range(col_max):
    op = matrix[-1][col]
    if op == '*':
        curr = 1
    else:
        curr = 0
    for row in range(row_max-1):
        if op == '*':
            curr*=int(matrix[row][col])
        else:
            curr+=int(matrix[row][col])
    result+=curr


print('-'*100)
print(result)

