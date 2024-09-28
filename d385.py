while 1:
    n=int(input())
    if n==0:
        break
    s=input().split()
    l=len(s)
    for i in range(l-1):
        for j in range(i+1, n):
            if s[i]+s[j]<s[j]+s[i]:
                s[i],s[j]=s[j],s[i]
    print(''.join(s))