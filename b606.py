while 1:
    n=int(input())
    if n==0:
        break
    s=list(map(int, input().split()))
    s.sort()
    total=0
    while len(s)!=1:
        num=0
        num+=s.pop(0)
        num+=s.pop(0)
        total+=num
        s.append(num)
        s.sort()
    print(total)