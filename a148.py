while 1:
    try:
        s=list(map(int, input().split()))
        n=s[0]
        ave=sum(s[1:])/(len(s)-1)
        if ave>59:
            print('no')
        else:
            print('yes')
    except:
        break