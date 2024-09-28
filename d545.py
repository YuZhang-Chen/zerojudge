n=int(input())
s=input().split()
m=int(input())
data=[]
for i in range(0,len(s)-1,2):
    data.append((int(s[i+1]),s[i]))
data.sort(reverse=True)
print(*data[m-1][::-1])