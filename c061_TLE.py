def fac(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum

while 1:
    n,m=map(int, input().split())
    if n==0 and m==0:
        break
    c=fac(n)/(fac(n-m)*fac(m))
    print(int(c))