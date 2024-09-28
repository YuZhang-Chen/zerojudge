cash=0
money=0
f=True
for i in range(1,13):
    cash+=300
    cash-=int(input())
    if cash>=100:
        while cash>=100:
            money+=100
            cash-=100
    if f:
        if cash<0:
            a=i
            f=False
if not f:
    print(-a)
else:
    print(int(money*1.2+cash))