while 1:
    try:
        n=int(input())
        s=list(map(int, input().split()))
        s1=sorted(list(set(s)))
        cnt=[]
        for i in s1:
            cnt.append(s.count(i))
        cnt1=sorted(cnt, reverse=True)
        for i in cnt1:
            print(s1[cnt.index(i)], end=' ')
            cnt[cnt.index(i)]=-1
        print()
    except:
        break