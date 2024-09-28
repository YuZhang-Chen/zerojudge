n,m=map(int, input().split())
lst=[]
for _ in range(n):
    a,b=map(int, input().split())
    lst.append([a,b])

lst=sorted(lst, reverse=True, key=lambda x:x[1])
ans=0
for i in range(n):
    if m==0:
        break
    while 1:
        if lst[i][0]==0 or m==0:
            break
        ans+=lst[i][1]
        lst[i][0]-=1
        m-=1
print(ans)