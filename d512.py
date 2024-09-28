while 1:
    try:
        n=int(input())
        s=list(map(int, input().split()))
        ans=[0]
        for i in range(len(s)):
            num=[]
            for j in range(len(ans)):
                num.append(s[i]+ans[j])
            ans+=num
        print(len(set(ans))-1)
    except:
        break