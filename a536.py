for _ in range(int(input())):
    e,f,c=map(int, input().split())
    sum_ef=e+f
    ans=0
    while sum_ef>=c:
        ans+=sum_ef//c
        sum_ef=sum_ef%c+sum_ef//c
        
    print(ans)