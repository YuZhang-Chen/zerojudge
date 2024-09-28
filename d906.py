m=int(input())
n=int(input())
data=[]
for _ in range(6):
    a,b,c=input().split()
    data.append((a,int(b),int(c)))
if m%2==1:
    data.sort(key=lambda x:x[1])
else:
    data.sort(key=lambda x:(x[2],x[1]))

seat=[0 for i in range(6)]
for i in range(6):
    seat[(i+n-1)%6]=data[i][0]
print(seat[1])