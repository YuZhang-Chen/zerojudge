for _ in range(int(input())):
    ans=[]
    a,b,c=map(int, input().split())
    for i in range(a+1,b):
        if i%c!=0:
            ans.append(i)
    
    if len(ans)==0:
        print('No free parking spaces.')
    else:
        print(*ans)