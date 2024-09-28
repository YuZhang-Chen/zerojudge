cnt=0
while True:
    try:
        if cnt>0:
            print()
        s=list(map(int, input().split()))
        n=s[0]
        x=s[1]
        s=s[2:]
        people=[i for i in range(1, n+1)]

        for i in s:
            idx=0
            f=0
            while len(people)>x:
                f=1
                idx+=i-1
                if idx>=len(people):
                    break
                people.pop(idx)
            if f==0:
                break
        cnt+=1
        print("Selection #%d"%(cnt))
        print(*people)
    except:
        break