n=int(input())
t=0
while n!=0:
    t+=1
    print('Game %d:'%(t))
    ans1=input().split()
    while True:
        A=0
        B=0
        ans=ans1.copy()
        s=input().split()
        if set(s)=={'0'}:
            break
        for i in range(len(s)):
            if ans[i]==s[i]:
                A+=1
                ans[i]='X'
                s[i]='XX'
        set1=list(set(ans)&set(s))
        for i in set1:
            B+=min(s.count(i), ans.count(i))
        print('    (%d,%d)'%(A, B))  
    n=int(input())