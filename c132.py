def f(k):
    k=k[::-1]
    sum=0
    for i in range(len(k)):
        sum+=(ord(k[i])-96)*(26**i)
    sum=str(sum)[::-1]
    ou=''
    for i in range(len(sum)-1,-1,-1):
        if i%3==2 and i!=len(sum)-1:
            ou+=','
        ou+=sum[i]
    return ou

def g(n):
    alpha=''
    while n>0:
        n1=n%26
        alpha+=chr(n1+96)
        n//=26
    return alpha[::-1]
    
while 1:
    s=input().strip()
    if s=='*':
        break
    if s.isalpha():
        ans1=s
        ans2=f(s)
    else:
        ans1=g(int(s))
        ans2=f(g(int(s)))
    
    print('%-21s %s'%(ans1,ans2))