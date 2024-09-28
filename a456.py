from itertools import combinations

for _ in range(int(input())):
    n=int(input())
    num=[i for i in range(1,n+1)]
    ans=[]
    for a in range(len(num)):
        for i in combinations(num, a+1):
            aa=list(i)
            ans.append(aa)
    print('{0}')
    for i in ans:
        print(str(i).replace('[','{').replace(']','}').replace(' ',''))
    print()