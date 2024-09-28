def f(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=f(parent[a])
        return parent[a]

n,m,q=map(int, input().split())
parent=[i for i in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    a=f(a)
    b=f(b)
    if a!=b:
        parent[b]=a

for _ in range(q):
    p,q=map(int, input().split())
    if f(p)==f(q):
        print(':)')
    else:
        print(':(')