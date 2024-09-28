n, m = map(int, input().split())
path = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

odd_vertex = 0
for i in range(1, n+1):
    if len(path[i])%2 == 1:
        odd_vertex += 1

if odd_vertex == 0 or odd_vertex == 2:
    print("YES")
else:
    print("NO")