for _ in range(int(input())):
    s=list(map(int, input().split()))
    del s[0]
    mx=-1e9
    sum=0
    for i in s:
        sum+=i
        if sum>mx:
            mx=sum
        if sum<0:
            sum=0
    print(mx)