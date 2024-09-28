while 1:
    try:
        s=input().split()
        n=int(s.pop(0))
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i]+s[j]<s[j]+s[i]:
                    s[i],s[j]=s[j],s[i]
        print(''.join(s))
    except:
        break