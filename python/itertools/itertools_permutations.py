import sys
from itertools import permutations

data = raw_input().strip().split(' ')

for x in sorted(list(permutations(data[0], int(data[1])))):
    print ''.join(x)