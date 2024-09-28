while 1:
    try:
        s=input().split('.')
        b=float('0.'+s[1])
        ans1=bin(int(s[0]))[2:]
        ans2=''
        cnt=1
        while b!=0:
            if b>=0.5**cnt:
                ans2+='1'
                b-=0.5**cnt
            else:
                ans2+='0'
            cnt+=1
        print(ans1,'.',ans2, sep='')
    except:
        break