prefix=[]
infix=[]
def travesal(n,ls,rs):
    global prefix,infix
    postfix=[]
    if ls==rs:
        return [prefix[n]]
    if ls>rs:
        return []

    pos=infix.index(prefix[n])
    N=[prefix[n]]
    L=travesal(n+1,ls,pos-1)
    R=travesal(n+(pos-ls)+1,pos+1,rs)
    if R==None:
        R=[]
    if L==None:
        L=[]
    for a in L:
        postfix.append(a)
    for a in R:
        postfix.append(a)
    for a in N:
        postfix.append(a)
    return postfix

while 1:
    try:
        prefix,infix=input().split()
        y=travesal(0,0,len(prefix)-1)
        print(''.join(y))
    except:
        break