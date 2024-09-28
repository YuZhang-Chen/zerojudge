from itertools import combinations
import math

while 1:
    n=int(input())
    if n==0: break
    num=[]
    for _ in range(n):
        num.append(int(input()))
    num1=list(combinations(num,2))
    num2=0
    for a,b in num1:
        if math.gcd(a,b)==1:
            num2+=1
    if num2==0:
        print('No estimate for this data set.')
    else:
        ans=math.sqrt((n*(n-1)/2)*6.0/num2)
        print('%.6f'%(ans))
