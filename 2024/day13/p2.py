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
    x_prize+=10000000000000
    y_prize+=10000000000000

    print("x1,y1",x1,y1)
    print("x2,y2",x2,y2)
    print("x_prize,y_prize",x_prize,y_prize)

    

    combinations = []

    for divisor in range(2,min(x_prize,y_prize)//2):
        
        if x_prize % divisor == 0 and y_prize%divisor ==0:
            new_x_prize = x_prize // divisor
            new_y_prize = y_prize // divisor
            print("Trying divisor", divisor)
            print("new_prizes", new_x_prize, new_y_prize)
            upper_limit_x1 = new_x_prize//x1 + 1
            upper_limit_y1 = new_y_prize//y1 + 1

            upper_limit_x2 = new_x_prize//x2 + 1
            upper_limit_y2 = new_y_prize//y2 + 1

            new_x_target = new_x_prize // divisor
            new_y_target = new_y_prize // divisor


            for b1 in range(0, min(upper_limit_x1, upper_limit_y1)):
                x , y = ( (x1*b1)  ) , ( (y1*b1) )

                if x > new_x_prize or y > new_y_prize:
                    break

                if (new_x_prize - x) % x2 == 0 and (new_y_prize - y) % y2 == 0 and (new_x_prize - x) / x2 == (new_y_prize - y) / y2:
                    b2 = (new_x_prize - x) // x2
                    b1*=divisor
                    b2*=divisor
                    combinations.append( (( b1*3 )+ ( b2*1 ), b1, b2) )
            
        
        # print(b1,b2, x- x_prize, y-y_prize)
        
    
    combinations.sort()

    if len(combinations)>0:
        print("Minimized: ", combinations[0])
        result+=combinations[0][0]
    else:
        print("None found")
    print("-"*100)
    

print("Result", result)
