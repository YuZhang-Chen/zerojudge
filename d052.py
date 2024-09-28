n=int(input())
s=list(map(int, input().split()))
mx=0
sum=0
for i in s:
    sum+=i
    mx=max(sum,mx)
    if sum<0:
        sum=0
print(mx)