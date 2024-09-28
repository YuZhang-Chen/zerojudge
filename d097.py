while 1:
    try:
        s=list(map(int, input().split()))
        n=s.pop(0)
        num=[i for i in range(1,n)]
        num1=[]
        for i in range(1,len(s)):
            num1.append(abs(s[i]-s[i-1]))

        if num==sorted(num1):
            print('Jolly')
        else:
            print('Not jolly')
    except:
        break