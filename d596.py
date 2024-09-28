lst=[[1,2,3],[4,5,6],[7,8,9]]

dxy=[(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(int(input())):
    num=[]
    a,b,c=map(int, input().split())
    for i in range(3):
        if a in lst[i]:
            y=i
            x=lst[i].index(a)
    for u,v in dxy:
        newr=y+u
        newc=x+v
        if 0<=newr<=2 and 0<=newc<=2:
            num.append(lst[newr][newc])

    num1=[]
    num2=[]
    for i in range(3):
        if b in lst[i]:
            y=i
            x=lst[i].index(b)
    for u,v in dxy:
        newr=y+u
        newc=x+v
        if 0<=newr<=2 and 0<=newc<=2:
            num1.append(lst[newr][newc])

    for i in range(3):
        if c in lst[i]:
            y=i
            x=lst[i].index(c)
    for u,v in dxy:
        newr=y+u
        newc=x+v
        if 0<=newr<=2 and 0<=newc<=2:
            num2.append(lst[newr][newc])
    
    ans=set(num)-set(num1)-set(num2)
    if ans==set():
        print('Empty')
    else:
        print(*sorted(list(ans)))