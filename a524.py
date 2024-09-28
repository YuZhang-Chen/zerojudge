from itertools import permutations

while 1:
    try:
        n=int(input())
        num=''.join([str(i) for i in range(n,0,-1)])
        ans=list(permutations(num))
        for i in ans:
            print(''.join(i))
    except:
        break