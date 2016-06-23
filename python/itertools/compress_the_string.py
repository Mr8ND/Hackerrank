import sys
from itertools import groupby

output_string = []
for k,g in groupby(sys.stdin.read()):
    output_string.append('''(%s, %s)'''% (len(list(g)), k))
print ' '.join(output_string)

