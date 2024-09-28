while 1:
    try:
        a,b=input().split()
        idx=0
        str1=''
        for i in b:
            if idx==len(a):
                break
            if a[idx]==i:
               str1+=a[idx]
               idx+=1
        if str1==a:
            print('Yes')
        else:
            print('No') 
    except:
        break