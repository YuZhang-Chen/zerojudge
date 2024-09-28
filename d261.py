n=int(input())
while n!=-1:
    a=1
    b=1
    b1=1
    if n==0:
        print(0,1)
    else:
        for i in range(2,n+1):
            b1,b=b,b1+b
            a+=b1
        print(a,a+b)
    n=int(input())