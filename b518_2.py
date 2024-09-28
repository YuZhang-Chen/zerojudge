for _ in range(int(input())):
    n=int(input())
    vertex=[[] for i in range(n)]
    for _ in range(n):
        a,b=map(int, input().split(','))
        if b==99:
            root=a
        else:
            vertex[a].append(b)
            vertex[b].append(a)
    ans={}
    visited=[]    
    def dfs(x,path=[]):
        visited.append(x)
        p=path.copy()
        r=0
        for i in vertex[x]:
            if i not in visited:
                r+=1
                p.append(i)
                dfs(i,p)
                p=path.copy()
        if r==0:
            ans[x]=path[:-1][::-1]

    dfs(root)
    t=sorted(list(ans))
    for i in t:
        if len(ans[i])==0:
            print('%d:N'%(i))
        else:
            ans1=','.join([str(i) for i in ans[i]])
            print('%d:{%s}'%(i,ans1))
    print()