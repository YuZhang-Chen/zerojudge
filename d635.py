while 1:
    n=int(input())
    if n<0:
        print(-1)
        break
    if n==0:
        print(0)
    else:
        ans=''
        while n>0:
            nn=n%8
            ans+=str(nn)
            n//=8
        print(ans[::-1])