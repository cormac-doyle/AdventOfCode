input_ = []

from collections import defaultdict
from functools import cache
device_map = defaultdict(list)

with open("input.txt") as file:
    for line in file:
        d1,d_list_str = line.strip().split(':')

        for d in d_list_str.split(' '):
            if d != '':
                device_map[d1].append(d)

print('-'*200)

paths = defaultdict( int )
keep_going= [True]

@cache
def p1(start, end):
    result = 0
    if start == end:
        return 1
    else:
        for d in device_map[start]:
            result+=p1(d,end)
    return result

@cache
def p2(start, end, seen_fft, seen_dac):
    result = 0
    if start == 'fft':
        seen_fft = True
    if start == 'dac':
        seen_dac = True
    if start == end and seen_dac and seen_fft:
        return 1
    else:
        for d in device_map[start]:
            result+=p2(d, end, seen_fft, seen_dac)
    return result

print( 'p2', p2('svr','out', False, False) )
