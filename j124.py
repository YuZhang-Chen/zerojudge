def dfs(r):
    global s,idx
    tot=0
    for i in range(2+r%2):
        u=s[idx]
        idx+=1
        if u>0:
            tot+=abs(r-u)+dfs(u)
    return tot

idx=1
s=list(map(int, input().split()))
print(dfs(s[0]))