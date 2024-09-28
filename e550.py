t=int(input())
for _ in range(t):
    if _==0:
        input()
    arr=[]
    a,b=map(int, input().split())
    while 1:
        try:
            s=list(input())
            if s==[]:
                break
            tt=['#']
            for i in range(len(s)):
                if s[i]=='1':
                    tt.append('#')
                elif s[i]=='0':
                    tt.append(0)
        except:
            break
        tt.append('#')
        arr.append(tt)
    arr.insert(0,['#']*(len(arr[0])))
    arr.append(['#']*(len(arr[0])))
    
    xy=[(-1,0),(0,1),(1,0),(0,-1)]
    q=[(a,b)]
    arr[a][b]='#'
    ans=0
    while len(q)>0:
        aa=q.pop(0)
        ans+=1
        y=aa[0]
        x=aa[1]
        for i in range(4):
            r=y+xy[i][0]
            c=x+xy[i][1]
            if arr[r][c]==0:
                q.append((r,c))
                arr[r][c]='#'
    print(ans)
    print()