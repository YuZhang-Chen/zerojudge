n,k,w=map(int, input().split())
ans=n
while n>=k:
    num=n//k*w
    ans+=num
    n=n%k+num
print(ans)