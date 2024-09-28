x=['','I','II','III','IV','V','VI','VII','VIII','IX']
y=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
h=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
t=['','M','MM','MMM']
sig=['I','V','X','L','C','D','M']
num=[1,   5,  10, 50, 100, 500, 1000]

def f(n):
    ans=''
    if n==0:
        ans='ZERO'
    else:
        it=n//1000
        ans+=t[it]
        ih=(n//100)%10
        ans+=h[ih]
        iy=(n//10)%10
        ans+=y[iy]
        ix=n%10
        ans+=x[ix]
    return ans

def g(key):
    ans=0
    for i in range(len(key)-1):
        k1=key[i]
        k2=key[i+1]
        p1=sig.index(k1)
        p2=sig.index(k2)
        a=num[p1]
        b=num[p2]
        if a>=b:
            ans+=a
        else:
            ans-=a
    k1=key[len(key)-1]
    p1=sig.index(k1)
    ans+=num[p1]
    return ans

for _ in range(int(input())):
    a,b=input().split()
    if a=='1':
        ans=g(b)
    elif a=='2':
        ans=f(int(b))
    print(ans)