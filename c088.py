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
    s=list(map(int, input().split()))
    if s[0]==0:
        break
    number=1
    for i in range(0,len(s)-1,2):
        number*=s[i]**s[i+1]
    num=[]
    f(number-1)
    num1=sorted(list(set(num)),reverse=True)
    for i in num1:
        print(i, num.count(i), end=' ')
    print()