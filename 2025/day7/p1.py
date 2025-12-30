
matrix = None

with open("input.txt") as file:
    matrix = [line.rstrip() for line in file]

beams = set()
beams.add(matrix[0].find('S'))

result=0
for line in matrix[1:]:
    for i, char in enumerate(line):
        if char == '^' and i in beams: 
            result+=1
            beams.add(i-1)
            beams.add(i+1)
            beams.remove(i)

print('\n','-'*100)
print(result)

