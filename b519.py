for _ in range(int(input())):
    s=list(map(int, input().split()))
    suit=[]
    number=[]
    for i in s:
        suit.append(i//13)
        number.append(i%13)
        
    number.sort()
    number1=[i for i in range(min(number),max(number)+1)]
    number2=list(set(number))
    cnt=sorted([number.count(i) for i in number2])

    if number==[1,10,11,12,13]:
        if len(set(suit))==1:
            ans=7
        else:
            ans=4
    elif number==number1 and len(set(suit))==1:
        ans=7
    elif cnt==[1,4]:
        ans=6
    elif cnt==[2,3]:
        ans=5
    elif number==number1:
        ans=4
    elif 3 in cnt:
        ans=3
    elif cnt==[1,2,2]:
        ans=2
    elif 2 in cnt:
        ans=1
    else:
        ans=0

    print(ans)