a=1
b=1
n=int(input())
for i in range(2,n+1):
    a,b=b,a+b
print(a,':',b,sep='')