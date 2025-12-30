from collections import defaultdict

matrix = None
with open("input.txt") as file:
    matrix = [line.rstrip() for line in file]

points = []
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
for i in range(len(points)-1):
    for j in range(i+1, len(points)):

        distances.append( (get_dist(points[i],points[j]),i,j) )
distances.sort()

'''
Iterate through each distance and pair of points and add points to circuits (list of sets)
There are three possibilities:
    1. Neither point is in a circuit: create a new circuit of those two points
    2. One or both points matches a single circuit: merge the current two points into that circuit
    3. Each point is in different circuits: create a new circuit merging all three. Remove the old circuits

This is a DSU (disjoint set union) data strucutre, a data structure that stores a collection of disjoint (non-overlapping) sets
'''

circuits = defaultdict(set)
result = None
for _, p1, p2 in distances:
    merged_circuit = set([p1,p2]).union(circuits[p1]).union(circuits[p2])
    c = min(merged_circuit)
    circuits[c] = merged_circuit

    # if the circuit we have just made combines all the points, return the result
    if len(merged_circuit) == len(matrix):
        result = points[p1][0] * points[p2][0]
        break

print('-'*100)
print(result)
