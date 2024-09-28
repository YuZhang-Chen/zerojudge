while 1:
    try:
        s=list(map(int, input().split()))
        n=s.pop(0)
        mx=-1e9
        sum=0
        for i in range(0,len(s)):
            sum+=s[i]
            mx=max(sum,mx)
            if sum<0:
                sum=0
        if mx<0:
            print(0)
        else:
            print(mx)
    except:
        break