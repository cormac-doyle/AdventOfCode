

points = []
with open("test.txt") as file:
    for line in file:
        x,y=line.strip().split(',')
        
        points.append(( int(x),int(y) ))



areas = []

for i in range(len(points)-1):
    for j in range(i,len(points)):
        x1 , y1 = points[i]
        x2 , y2 = points[j]

        area = (abs(x1-x2) + 1) * ( abs(y1-y2) +1)
        #print( points[i] , points[j], area)
        areas.append(area)

areas.sort()

print(areas[-1])
