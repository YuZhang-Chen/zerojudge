while 1:
    try:
        n=eval(input())
        num=0
        x=2
        cnt=0
        while num<n:
            num+=1/x
            x+=1
            cnt+=1
        print(cnt, 'card(s)')
    except:
        break