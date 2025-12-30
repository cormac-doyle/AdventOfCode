input_ = []

with open("input.txt") as file:
    for line in file:
        l = line.strip().split(' ')
        lights = tuple(l[0][1:-1])
        buttons_list = []
        

        for buttons in l[1:-1]:
            curr = []
            for b in buttons[1:-1].split(','):
                curr.append(int(b))
            buttons_list.append(curr)

        input_.append( (lights, buttons_list ))

def press_buttton(curr_state, button):
    next_ = list(curr_state)
    for idx in button:
        if next_[idx] == '.':
            next_[idx] = '#'
        else:
            next_[idx] = '.'
    
    return tuple(next_)

def bfs(states, buttons, goal_state):
    count = 0
    memo = set()
    while True:
        next_states = set()
        count+=1
        for curr_state in states:
            for b in buttons:
                next_state = press_buttton(curr_state, b)
                if next_state == goal_state:
                    return count
                elif next_state not in memo:
                    memo.add( next_state )
                    next_states.add( next_state )
        states = next_states

res = 0
for goal_state , buttons in input_:
    starting = tuple('.'*len(goal_state))
    states = set([starting])

    ans = bfs( states, buttons, goal_state)
    res+=ans


print('-'*100)
print("RESULT:",res)

