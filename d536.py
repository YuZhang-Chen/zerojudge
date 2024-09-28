dic={}
m=int(input())
for _ in range(m):
    s=list(input())
    a,b=s[0],s[1]
    if a not in dic:
        dic[a]=[b]
    else:
        dic[a]+=[b]

ans=[]
for x in dic:
    q=[(x,0)]
    distance={}
    visited=[]
    idx=x
    while len(q)>0:
        aa=q.pop(0)
        node=aa[0]
        d=aa[1]
        if node in dic:
            for i in dic[node]:
                if i==x:
                    ans.append(d+1)
                if i not in visited:
                    visited.append(i)
                    q.append((i,d+1))
                    distance[i]=d+1
if len(ans)==0:
    print(0)
else:
    print(min(ans))