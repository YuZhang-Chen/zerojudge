def f(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

while 1:
    try:
        s=list(input())
        num=''
        front=0
        num+=s[front]
        prm=[]
        while front!=len(s)-1:
            front+=1
            if f(int(num)):
                prm.append(int(num))
                num=''
            num+=s[front]

        if f(int(num)):
            prm.append(int(num))
        print(len(prm))
        
        if len(prm)!=0:
            for i in prm:
                print(i)
            print()
    except:
        break