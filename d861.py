def f(n,ls,rs):
    prefix=[]
    if ls==rs:
        return [postfix[n]]
    if ls>rs:
        return []
    
    pos=infix.index(postfix[n])
    N=[postfix[n]]
    R=f(n-1,pos+1,rs) #右子樹
    L=f(n-(rs-pos)-1, ls, pos-1)
    if R==None:
        R=[]
    if L==None:
        L=[]
    for a in N:
        prefix.append(a)
    for a in L:
        prefix.append(a)
    for a in R:
        prefix.append(a)
    print(N)
    return prefix

infix=list(input())
postfix=list(input())
ans=f(len(postfix)-1,0,len(postfix)-1)
print(''.join(ans))