while 1:
    try:
        n,t=map(int, input().split())
        time=[0 for i in range(t)]
        for _ in range(n):
            s=input().split()
            for i in range(len(s)):
                ss=s[i].split(':')
                time[i]+=int(ss[0])*60+int(ss[1])

        data=sorted(time)
        for i in data:
            print(time.index(i)+1,i)
            time[time.index(i)]='X'
    except:
        break