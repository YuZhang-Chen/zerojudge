while 1:
    a,b,c,d=map(int, input().split())
    if a==0 and b==0 and c==0 and d==0:
        break
    ans=1080
    ans+=(40+a-b)%40*9
    ans+=(40+c-b)%40*9
    ans+=(40+c-d)%40*9
    print(ans)
