from itertools import combinations_with_replacement
import sys

data = sys.stdin.read().split(' ')

def print_combination_function(string, k, func):
    values = [ ''.join(sorted(x)) for x in list(func(string, k))]
    for value in sorted(values):
        print (''.join(value))

print_combination_function(data[0], int(data[1]), combinations_with_replacement)

