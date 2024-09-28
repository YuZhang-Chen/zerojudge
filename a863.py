while 1:
    try:
        num=[]
        n=int(input())
        n1=n
        while 1:
            sum=0
            n1=str(n1)
            for i in range(len(n1)):
                sum+=int(n1[i])**2
            if sum in num:
                f=False
                break
            if sum==1:
                f=True
                break
            num.append(sum)
            n1=sum
        if f:
            print(n,'is a happy number')
        else:
            print(n,'is an unhappy number')
    except:
        break
    
    