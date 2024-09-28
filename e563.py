for _ in range(int(input())):
    data=[]
    while 1:
        s,f=map(int, input().split())
        if s==0 and f==0:
            break
        data.append((s,f))
    h=[0 for _ in range(10)]
    data.sort(key=lambda x:x[1])
    cnt=0
    for a,b in data:
        for j in range(a,b):
            if h[j]==1:
                break
        else:
            cnt+=1
            for j in range(a,b):
                h[j]=1
    print(cnt)