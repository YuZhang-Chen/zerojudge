for xx in range(int(input())):  
    nnn=input().split()
    n=int(nnn[-1])
    a=[]
    f=True
    for i in range(n):
        s=list(map(int, input().split()))
        num=[]
        for i in s:
            if i<0:
                f=False
            num.append(i)
        a.append(num)
    b=[]
    for i in range(len(a)):
        b.append(a[i][::-1])
    b=b[::-1]
    
    if not f:
        print('Test #%d: Non-symmetric.'%(xx+1))
    elif a==b:
        print('Test #%d: Symmetric.'%(xx+1))
    else:
        print('Test #%d: Non-symmetric.'%(xx+1))