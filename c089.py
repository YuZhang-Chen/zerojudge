number=[i for i in range(0,16)]
key=[str(i) for i in range(0,10)]+['A','B','C','D','E','F']

while 1:
    try:
        a,b,c=input().split()
        b,c=int(b),int(c)
        num=int(a,b)
        ans=''
        while num!=0:
            nn=num%c
            ans+=key[number.index(nn)]
            num//=c
        if len(ans)>7:
            print('%7s'%('ERROR'))
        else:
            print('%7s'%(ans[::-1]))
    except:
        break