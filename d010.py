while 1:
    try:
        n=int(input())
        num=[]
        for i in range(1,n):
            if n%i==0:
                num.append(i)

        if sum(num)>n:
            print('盈數')
        elif sum(num)<n:
            print('虧數')
        else:
            print('完全數')
    except:
        break