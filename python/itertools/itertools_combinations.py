from __future__ import print_function
from itertools import combinations
import sys

data = sys.stdin.read().split(' ')

def print_combination_function(string, k):
    values = [ ''.join(sorted(x)) for x in list(combinations(string, k))]
    for value in sorted(values):
        print (''.join(value))
    
map(lambda x: print_combination_function(data[0], x), [int(x) for x in range(1, int(data[1]) + 1)]) 