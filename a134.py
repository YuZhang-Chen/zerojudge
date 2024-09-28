fib=[1,1]
for i in range(2,45):
    f=fib[i-1]+fib[i-2]
    fib.append(f)

for _ in range(int(input())):
    n=int(input())
    n1=n
    ans=''
    while n>0:
        for i in fib[::-1][:-1]:
            if i<=n:
                ans+='1'
                n-=i
            else:
                ans+='0'
    print(n1,'=',int(ans),'(fib)')