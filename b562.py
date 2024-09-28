while 1:
    try:
        s=input()[::-1]
        ans=0
        num=0
        for i in range(len(s)):
            if s[i]=='1':
                if i%2==0:
                    ans+=2**i
                else:
                    ans+=-2**i
        print(ans)
    except:
        break