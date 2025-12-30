from collections import defaultdict

import heapq

matrix = None
with open("input.txt") as file:
    matrix = [line.rstrip() for line in file]

points = []
heapq.heapify(points)
for line in matrix:
    x,y,z = line.split(',')
    points.append( ( int(x), int(y), int(z)) )

'''
Get quadratic distance between two points
'''
def get_dist(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2

    dist = ( 
        ( (x2-x1) ** 2 ) + 
        ( (y2-y1) ** 2 ) +  
        ( (z2-z1) ** 2 ) 
    )
    return dist

'''
Calculate all distances from one point to another

Sort the distances, so we have the shortest ones

To optimize use a heap and insert into the heap ?
'''
distances = []
heapq.heapify(distances)
for i, p1 in enumerate(points[:-1]):
    for p2 in points[i+1:]:
        heapq.heappush(distances, (get_dist(p1,p2),p1,p2))

'''
Iterate through each distance and pair of points and add points to circuits (list of sets)
There are three possibilities:
    1. Neither point is in a circuit: create a new circuit of those two points
    2. One or both points matches a single circuit: merge the current two points into that circuit
    3. Each point is in different circuits: create a new circuit merging all three. Remove the old circuits

This is a DSU (disjoint set union) data strucutre, a data structure that stores a collection of disjoint (non-overlapping) sets
'''
circuits = []
result = None
for _, p1,p2 in distances:
    inclusion_indexs = []
    for i in range(len(circuits)):
        if p1 in circuits[i] or p2 in circuits[i]:
            inclusion_indexs.append(i)

    if len(inclusion_indexs) == 0:
        next_circuit = set([p1,p2])
        circuits.append(next_circuit)
    elif len(inclusion_indexs) == 1:
        circuits[inclusion_indexs[0]].add(p1)
        circuits[inclusion_indexs[0]].add(p2)
    else:
        next_circuit = set([p1,p2]).union(circuits[inclusion_indexs[0]]).union(circuits[inclusion_indexs[1]])
        del circuits[inclusion_indexs[1]]
        del circuits[inclusion_indexs[0]]
        circuits.append(next_circuit)

    # if the circuit we have just made combines all the points, return the result
    if len(circuits) == 1 and len(circuits[0]) == len(matrix):
        x1,_,_ = p1
        x2,_,_ = p2
        result = x1*x2
        break

print('-'*100)
print(result)
