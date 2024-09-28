for _ in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    mx=max(s)
    mn=min(s)
    print((mx-mn)*2)