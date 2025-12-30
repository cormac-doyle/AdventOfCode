import operator
matrix = None

with open("input.txt") as file:
    matrix = []
    for i, line in enumerate(file):
        matrix.append(list(line.rstrip('\n')))

row_max = len(matrix)
col_max = len(matrix[0])

result = 0

def calc( start, end, operation):
    operations_map = {
        '+': (0, operator.add),
        '*': (1, operator.mul)
    }
    res, op = operations_map[operation]

    for idx in range(start, end):
        curr_num = ''
        for row in range(row_max-1):
            if matrix[row][idx] != ' ':
                curr_num+=matrix[row][idx]

        res = op(res, int(curr_num))
    return res

operations = matrix[-1]
del matrix[-1]


idx_start = 0
for idx in range(1, len(operations)):
    if operations[idx] in ['*', '+']:
        result += calc(idx_start, idx-1, operations[idx_start])
        idx_start = idx

result += calc( idx_start , len(operations), operations[idx_start])

print('-'*100)
print(result)
