import sys
from itertools import product

A = raw_input().strip().split(' ')
B = raw_input().strip().split(' ')

print ' '.join(['''(%s, %s)'''%(x[0], x[1]) for x in list(product(A,B))])