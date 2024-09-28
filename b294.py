n=int(input())
day=list(map(int, input().split()))
total=0
for i in range(len(day)):
    total+=(i+1)*day[i]
print(total)