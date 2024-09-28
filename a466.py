for _ in range(int(input())):
    s=input()
    if len(s)==3:
        cnt=0
        for i in range(len(s)):
            if s[i]=='one'[i]:
                cnt+=1
        if cnt>=2:
            print(1)
        else:
            print(2)
    else:
        print(3)