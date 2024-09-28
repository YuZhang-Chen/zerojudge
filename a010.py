num=[]
def f(n):
    k=0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            k=i
            break
    if k!=0:
        num.append(k)
        f(n//k)
    else:
        num.append(n)

n=int(input())
f(n)
ans=''
num1=sorted(list(set(num)))
for i in range(len(num1)):
    cnt=num.count(num1[i])
    if i>0:
        ans+=' * '
    if cnt>1:
        ans+=str(num1[i])+'^'+str(cnt)
    else:
        ans+=str(num1[i])
print(ans)