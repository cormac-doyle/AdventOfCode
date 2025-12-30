input_ = []

with open("test.txt") as file:
    for line in file:
        l = line.strip().split(' ')
        joltages_str = l[-1][1:-1]
        buttons_list = []
        joltages = []
        for j in joltages_str.split(','):
            joltages.append(int(j))

        for buttons in l[1:-1]:
            curr = []
            for b in buttons[1:-1].split(','):
                curr.append(int(b))
            buttons_list.append(curr)

        input_.append( (joltages, buttons_list ))


def increase_joltage(curr_joltage, button, goal_state):
    next_ = list(curr_joltage)
    for idx in button:
        next_[idx]+=1
    return tuple(next_)


def bfs(states, curr_count, buttons, goal_state, memo):

    next_states = set()
    for curr_state in states:
        
        for b in buttons:
            next_state = increase_joltage(curr_state, b, goal_state)

            if next_state == goal_state:
                return curr_count
            else:
                for i in range(len(next_state)):
                    if next_state[i] > goal_state[i]:
                        break
                else:
                    if next_state not in memo:
                        next_states.add( next_state )
                        memo.add(next_state)

    curr_count+=1

    if len(next_states) > 0:
        return bfs(next_states, curr_count, buttons, goal_state, memo)

res = 0
for l in input_:
    answers = []
    goal_state , buttons = l
    starting = tuple([0]*len(goal_state))
    start = set()
    start.add(starting)
    memo = set()
    memo.add(starting)
    min_ = bfs( start, 1, buttons, tuple(goal_state), memo)
    res+=min_

print('-'*100)
print("RESULT:",res)

