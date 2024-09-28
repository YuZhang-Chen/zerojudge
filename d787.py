for _ in range(int(input())):
    a,b=input().split()
    a=a[::-1]
    b=b[::-1]
    if len(a)>len(b):
        a,b=b,a
    for i in range(len(b)-len(a)):
        a+='0'
    
    cnt=0
    c=False
    for i in range(len(a)):
        if not c:
            if int(a[i])+int(b[i])>=10:
                cnt+=1
                c=True
        elif c:
            if int(a[i])+int(b[i])+1>=10:
                cnt+=1
            else:
                c=False
    print(cnt)