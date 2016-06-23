import sys
from itertools import product

first_line = raw_input().strip()
k, m = int(first_line.split(' ')[0]), int(first_line.split(' ')[1])
k_list = []
for n in range(k):
    k_list.append((raw_input().strip()).split(' ')[1:])
    
possible_permutations = list(product(*k_list))
def squareOfTuple(l):
    return sum([int(x)**2 for x in list(l)])

tuple_list = []
for perm in possible_permutations:
    tuple_list.append((perm, squareOfTuple(perm) % m))
print sorted(tuple_list, key=lambda x: x[1], reverse=True)[0][1]