while 1:
    try:
        n=int(input())
        s=list(map(int, input().split()))
        s1=list(set(s))
        s1=sorted(s, reverse=True)

        for i in s:
            print(s1.index(i)+1, end=' ')
    except:
        break