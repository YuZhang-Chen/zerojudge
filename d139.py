while True:
    try:
        s=input()+"0"
        pre=None
        ans=""
        t=""
        for i in range(len(s)):
            if s[i]!=pre:
                if t!="":
                    ans+=t if len(t)<=2 else str(len(t))+t[0]
                t=""
                t+=s[i]
            else:
                t+=s[i]
            pre=s[i]
        print(ans)
    except:
        break