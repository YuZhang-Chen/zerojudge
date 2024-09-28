n,m=map(int, input().split())
a=[]
for i in range(n):
    s=['#']+input().split()+['#']
    a.append(s)
a.insert(0,['#']*(m+2))
a.append(['#']*(m+2))

dx=(0,0,1,-1)
dy=(1,-1,0,0)
for _ in range(int(input())):
    num=[]
    a1=a.copy()
    t=input()
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a1[i][j]==t:
                cnt=1
                a1[i][j]='#'
                q=[(i,j)]
                while len(q)>0:
                    aa=q.pop(0)
                    y=aa[0]
                    x=aa[1]
                    for i in range(4):
                        r=dy[i]+y
                        c=dx[i]+x
                        if a1[r][c]==t:
                            cnt+=1
                            a1[r][c]='#'
                            q.append((r,c))
                num.append(cnt)

    if max(num)<2:
        print(0)
    else:
        print(max(num))