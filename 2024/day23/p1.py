from collections import defaultdict

with open('input.txt') as f:
    data = f.read().strip()

data = data.split('\n')

connections = []
connections_map = defaultdict(set)

for l in data:
    s = l.split('-')
    connections.append( (s[0],s[1]) )
    connections_map[s[0]].add(s[1])
    connections_map[s[1]].add(s[0])


for el in connections_map.keys():
    print(el, ':', connections_map[el])

circuit_set = set()

# find pairs of 3
for el in connections_map.keys():
    for second_el in connections_map[el]:
        
        for third_el in connections_map[second_el]:
            for fourth_el in connections_map[third_el]:
                if fourth_el == el:
                    
                    circuit = [el, second_el, third_el]
                    circuit.sort()
                    circuit_set.add(tuple(circuit))

result = 0
for circuit in circuit_set:
    for el in circuit:
        if el[0] == 't':
            result+=1
            break

print("Result", result)