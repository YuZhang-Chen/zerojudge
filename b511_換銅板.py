n=int(input())
s=list(map(int, input().split()))
cash=int(input())

ans=[]
x=[]
def f(x):
    l=len(x)
    if l==n:
        tot=0
        for i in range(0,l):
            tot+=s[i]*x[i]
        if tot==cash:
            ans.append(x)
        return
    for i in range(0, cash//s[l]+1):
        f(x+[i])
f(x)
for i in ans:
    i=str(i).replace(' ','')
    print('('+i[1:-1]+')')