import sys
from itertools import combinations

n = float(raw_input().strip())
string = raw_input().strip()
k = int(raw_input().strip())

combined_string = list(combinations(string.split(' '), k))
output = [1 if 'a' in ''.join(list(tup)) else 0 for tup in combined_string]
print float(sum(output))/len(combined_string)