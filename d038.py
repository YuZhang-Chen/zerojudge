while 1:
    n=int(input())
    if n==0:
        break
    a=1
    b=1
    for i in range(2,n+1):
        a,b=b,a+b
    print(b)