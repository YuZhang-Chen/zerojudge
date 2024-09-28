fib=[0,1,1]
for i in range(3,31):
    fib.append(fib[i-1]+fib[i-2])

n=int(input())
for aaa in range(n):
    a,b=map(int, input().split())
    idx1=-1
    idx2=-1
    if a>b:
        a,b=b,a
    num=[]
    for i in range(len(fib)):
        if fib[i]>=a and fib[i]<=b:
            num.append(i)
    if len(num)==0:
        print(0)
    else:
        idx1=min(num)
        idx2=max(num)
        cnt=0
        if idx1!=-1 and idx2!=-1:
            for i in range(idx1, idx2+1):
                cnt+=1
                print(fib[i])
        print(cnt)

    if aaa!=n-1:
        print('------')