input_ = []

with open('input.txt') as f:
    data = f.read().strip()

data = data.split('\n')
for i in range(len(data)-1,-1,-1):
    if data[i] == '':
        del data[i]

print(data)

def parse_button(line):
    parts = line.split(' ')
    X = parts[2][2:-1]
    Y = parts[3][2:]
    return int(X), int(Y)

def parse_prize(line):
    parts = line.split(' ')
    X = parts[1][2:-1]
    Y = parts[2][2:]
    return int(X), int(Y)

games = []
result = 0
for i in range(0,len(data),3):
    x1,y1 = parse_button(data[i])
    x2,y2 = parse_button(data[i+1])
    x_prize,y_prize = parse_prize(data[i+2])

    print("x1,y1",x1,y1)
    print("x2,y2",x2,y2)
    print("x_prize,y_prize",x_prize,y_prize)

    upper_limit_x1 = x_prize//x1
    upper_limit_y1 = y_prize//y1

    upper_limit_x2 = x_prize//x2
    upper_limit_y2 = y_prize//y2

    combinations = []

    for b1 in range(0,max(upper_limit_x1, upper_limit_y1)):
        for b2 in range(0,max(upper_limit_x2, upper_limit_y2)):
            x , y = ( (x1*b1) + (x2*b2) ) , ( (y1*b1) + (y2*b2) )
            if x == x_prize and y == y_prize:
                combinations.append( (( b1*3 )+ ( b2*1 ), b1, b2) )
    
    combinations.sort()
    if len(combinations)>0:
        print("Minimized: ", combinations[0])
        result+=combinations[0][0]
    else:
        print("None found")
    print("-"*100)
    

print("Result", result)
