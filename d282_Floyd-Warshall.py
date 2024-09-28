cnt=0
while 1:
    n,m=map(int, input().split())
    if n==0:
        break
    cnt+=1
    mp=[0]
    a=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i!=j:
                a[i][j]=1e9
    
    for i in range(n):
        mp.append(input())
    for i in range(0,m):
        x,y,z=map(int, input().split())
        a[x][y]=z
        a[y][x]=z
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if a[j][i]+a[i][k]<a[j][k]:
                    a[j][k]=a[j][i]+a[i][k]
    mn=1e9
    for i in range(1,n+1):
        ans=0
        for j in range(1,n+1):
            ans+=a[i][j]
        if ans<mn:
            mn=ans
            idx=i
    print('Case #%d : %s'%(cnt, mp[idx]))