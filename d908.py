def dfs(start,total):
    if start not in G:
        return total
    mx=0
    for nxt, w in G[start]:
        mx=max(mx,dfs(nxt,total+w))
    return mx

G={}
s=input()
for _ in range(int(input())):
    tmp=input().split()
    if tmp[0] in G:
        G[tmp[0]].append((tmp[1],int(tmp[2])))
    else:
        G[tmp[0]]=[(tmp[1],int(tmp[2]))]
ans=dfs(s,0)
print(ans)