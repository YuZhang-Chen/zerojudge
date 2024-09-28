n=int(input())
s=sorted(list(map(int, input().split())))
if len(s)%2==1:
    print(s[len(s)//2])
else:
    a=s[len(s)//2-1]
    b=s[len(s)//2]
    suma=0
    sumb=0
    for i in range(len(s)):
        if i==len(s)//2-1:
            continue
        suma+=abs(s[len(s)//2]-s[i])
    for i in range(len(s)):
        if i==len(s)//2:
            continue
        sumb+=abs(s[len(s)//2]-s[i])

    if suma==sumb:
        print(a)
    elif suma>sumb:
        print(b)
    else:
        print(a)