from collections import defaultdict

import heapq
 

CONNECTIONS = 1000
matrix = None
with open("input.txt") as file:
    matrix = [line.rstrip() for line in file]

points = []
for line in matrix:
    x,y,z = line.split(',')
    points.append( (int(x),int(y),int(z)) )

def get_dist(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    
    dist = ( 
        ( (x2-x1)*(x2-x1) ) + 
        ( (y2-y1)*(y2-y1) ) +  
        ( (z2-z1)*(z2-z1) ) 
    )
    
    return dist

# ( dist, p1, p2 )
matched_points = []

for i in range(len(points)-1):
    for j in range(i+1,len(points)):
        p1 = points[i]
        p2 = points[j]

        distance = get_dist(p1,p2)
        matched_points.append( (distance,p1,p2) )


matched_points.sort()

circuits = []
matched_points = matched_points[:CONNECTIONS]
for _, p1,p2 in matched_points:
    inclusions = 0
    inclusion_indexs = []
    for i in range(len(circuits)):
        if p1 in circuits[i] or p2 in circuits[i]:
            inclusion_indexs.append(i)
            

    if len(inclusion_indexs)==0:
        next_circuit = set([p1,p2])
        circuits.append(next_circuit)
    elif len(inclusion_indexs) == 1:
        circuits[inclusion_indexs[0]].add(p1)
        circuits[inclusion_indexs[0]].add(p2)
    else:
        next_circuit = set([p1,p2])
        next_circuit = next_circuit.union(circuits[inclusion_indexs[0]])
        next_circuit = next_circuit.union(circuits[inclusion_indexs[1]])
        del circuits[inclusion_indexs[1]]
        del circuits[inclusion_indexs[0]]

        circuits.append(next_circuit)


biggest = []
for c in circuits:
    biggest.append(len(c))

biggest = sorted(biggest, reverse=True)
result=1
for score in biggest[:3]:
    result*=score

print('-'*100)
print(result)
