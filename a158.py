from math import gcd

for _ in range(int(input())):
    s=list(map(int, input().split()))
    mx=[]
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            mx.append(gcd(s[i],s[j]))
    print(max(mx))