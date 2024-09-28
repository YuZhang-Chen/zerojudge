def f(n):
    num=[]
    for i in range(1,n):
        if n%i==0:
            num.append(i)
    return sum(num)

ff=True
print('PERFECTION OUTPUT')
while 1:
    s=list(map(int, input().split()))
    for i in s:
        if i==0:
            ff=False
            break
        print('%5d'%(i), end='  ')
        if f(i)>i:
            print('ABUNDANT')
        elif f(i)<i:
            print('DEFICIENT')
        else:
            print('PERFECT')
    if not ff:
        break
print('END OF OUTPUT')