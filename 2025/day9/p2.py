

points = []
max_x = -float('inf')
min_x = float('inf')
max_y = -float('inf')
min_y = float('inf')

with open("input.txt") as file:
    for line in file:
        x,y=line.strip().split(',')
        x=int(x)
        y=int(y)

        points.append(( x,y ))
        max_x = max(max_x,x)
        min_x = min(min_x,x)
        max_y = max(max_y,y)
        min_y = min(min_y,y)


from collections import defaultdict
ranges_x = defaultdict(list)
ranges_y = defaultdict(list)


# areas = []
greens = []
points.append(points[0])
for i in range(len(points)-1):
        x1 , y1 = points[i]
        x2 , y2 = points[i+1]
        greens.append( ( ( min(x1,x2), max(x1,x2) ), (min(y1,y2),max(y1,y2)) ))


areas = []

for i in range(len(points)-1):
    for j in range(i,len(points)):
        x1 , y1 = points[i]
        x2 , y2 = points[j]

        area = (abs(x1-x2) + 1) * ( abs(y1-y2) +1)
        ##print( points[i] , points[j], area)
        areas.append( ( area, points[i], points[j] ))

areas = sorted(areas, reverse = True)



max_x_range = range(min_x,max_x)
max_y_range = range(min_y,max_y)


# print('greens ', greens)
def check_inside(x1,y1,x2,y2):

    for g in greens:
        gx,gy = g
        gxMin,gxMax = gx
        gyMin,gyMax = gy
        if gxMin < max(x1,x2) and gxMax > min(x1,x2) and  gyMin < max(y1,y2) and gyMax > min(y1,y2):
            return False

    return True

valid_areas = []
idx = 0
for a, p1,p2 in areas:
    #print (a, p1,p2)
    x1,y1 = p1
    x2,y2 = p2
    if check_inside(x1,y1,x2,y2):
        print('winner', p1,p2)
        print(a)
        break
    idx+=1


