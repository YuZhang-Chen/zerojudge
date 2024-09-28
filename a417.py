t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    if m == 1:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if m == 2:
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    step = 0
    row = 0
    col = 0
    for i in range(n**2):
        matrix[row][col] = i+1
        r, c = dir[step%4]
        if row+r < 0 or row+r >= n or col+c < 0 or col+c >= n or matrix[row+r][col+c] != 0:
            step += 1
            r, c = dir[step%4]
        row += r
        col += c

    for i in range(n):
        for j in range(n):
            print("%5d"%(matrix[i][j]), end="")
        print()
    
    for i in matrix:
        print(i)