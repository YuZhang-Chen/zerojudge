while 1:
    try:
        a=list(map(int, input().split()))
        b=list(map(int, input().split()))
        del a[0]
        del b[0]
        sum1=0
        sum2=0
        for i in range(len(a)):
            if a[i]==20:
                sum1+=(10*10)*3.14159
            if a[i]==16:
                sum1+=(8*8)*3.14159
            if a[i]==12:
                sum1+=(6*6)*3.14159
            if a[i]==9:
                sum1+=(4.5*4.5)*3.14159
            if a[i]==6:
                sum1+=(3*3)*3.14159
        for i in range(len(b)):
            if b[i]==20:
                sum2+=(10*10)*3.14159
            if b[i]==16:
                sum2+=(8*8)*3.14159
            if b[i]==12:
                sum2+=(6*6)*3.14159
            if b[i]==9:
                sum2+=(4.5*4.5)*3.14159
            if b[i]==6:
                sum2+=(3*3)*3.14159
                
        print('%.2f'%(abs(sum1-sum2)))
    except:
        break