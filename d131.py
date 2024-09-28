fac=[0,1]
for i in range(2, 101):
    fac.append(fac[-1]*i)

def f(n):
    k=0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            k=i
            break
    if k!=0:
        num.append(k)
        f(n//k)
    else:
        num.append(n)

while 1:
    n1=int(input())
    if n1==0:
        break
    num=[]
    n=fac[n1]
    f(n)
    num1=sorted(list(set(num)))
    ans=[]
    for i in num1:
        ans.append(num.count(i))

    print('%3d! ='%(n1), end='')
    for i in range(len(ans)):
        if i%15==0 and i!=0:
            print()
            print(' '*(9-len(str(ans[i]))), end='')
        print('%3d'%(ans[i]), end='')
    print()