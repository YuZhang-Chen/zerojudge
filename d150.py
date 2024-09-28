for _ in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    s.sort(reverse=True)
    ans=0
    while len(s)>2:
        s.pop(0)
        s.pop(0)
        ans+=s.pop(0)
    print(ans)