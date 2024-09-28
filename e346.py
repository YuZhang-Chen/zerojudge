n=int(input())
s=[0]+list(map(int, input().split()))
for i in range(2,n+1):
    s[i]+=s[i-1]

for _ in range(int(input())):
    a,b=map(int, input().split())
    print(s[b]-s[a-1])