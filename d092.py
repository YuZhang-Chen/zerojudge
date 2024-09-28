while 1:
    data=[]
    n=int(input())
    if n==0:
        break
    for _ in range(n):
        a,b=map(int, input().split())
        if a>b:
            data.append((2,'>',a+b))
        elif a<b:
            data.append((0,'<',a+b))
        else:
            data.append((1,'=',a+b))
    data.sort(key=lambda x:(-x[2],-x[0]))
    for i in data:
        print(i[1]+str(i[2]), end=' ')
    print()