for _ in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    B=[]
    for i in range(1,len(s)):
        cnt=0
        for j in range(0,i):
            if s[j]<=s[i]:
                cnt+=1
        B.append(cnt)
    print(sum(B))