for _ in range(int(input())):
    input()
    cnt=0
    s=list(map(int, input().split()))
    for j in range(len(s)-1):
        for i in range(len(s)-1-j):
            if s[i]>s[i+1]:
                cnt+=1
                s[i],s[i+1]=s[i+1],s[i]
    print('Optimal train swapping takes',cnt,'swaps.')