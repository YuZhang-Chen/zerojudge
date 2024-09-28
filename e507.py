while 1:
    try:
        a=list(input())
        b=list(input())
        ans=[]
        for i in range(len(a)):
            if a[i] in b:
                ans.append(a[i])
                b[b.index(a[i])]='_'
        ans.sort()
        print(''.join(ans))
    except:
        break