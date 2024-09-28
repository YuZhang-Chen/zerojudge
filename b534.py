import math
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

def g(n):
    if n<2:
        return 'N'
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 'N'
    return 'Y'

for _ in range(int(input())):
    a,b=map(int, input().split())
    num=[]
    f(a)
    num1=sorted(list(set(num)))
    ans1=''
    for i in num1:
        ans1+='*'
        if num.count(i)>1:
            ans1+=str(i)+'^'+str(num.count(i))
        else:
            ans1+=str(i)
    ans1=ans1[1:]
    ans2=str(math.gcd(a,b))
    ans3=g(int(ans2))
    print(ans1+' , '+ans2+' , '+ans3)