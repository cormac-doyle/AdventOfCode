
HEIGHT = 3 
WIDTH = 5

def check_tree(matrix):
    left =  0
    right =  WIDTH - 1

    for r in range(HEIGHT-1,-1,-1):
        print(r,left,r,right)
        if matrix[r][left] != 1 or matrix[r][right] != 1:
            # print("False",r,c)
            return False
        left+=1
        right-=1
    return True

tree = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
]
print("Check tree test", check_tree(tree))