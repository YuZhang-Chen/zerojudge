from decimal import *

t=int(input())
for _ in range(t):
    n=int(input())
    n*=Decimal(567)
    n/=Decimal(9)
    n+=Decimal(7492)
    n*=Decimal(235)
    n/=Decimal(47)
    n-=Decimal(498)
    n=str(n).split('.')
    n=n[0]
    ans=n[-2]
    print(ans)