from itertools import permutations
from sys import stdin

n=int(stdin.readline())
arr=[str(i) for i in range(1,n+1)]
ans=permutations(arr)
for i in ans:
    print(*i)