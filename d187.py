number=[1,2,3]*5
number+=[1,2,3,4]
number+=[1,2,3]
number+=[1,2,3,4]
alpha=[chr(i) for i in range(97,123)]

for x in range(int(input())):
    sum=0
    s=input()
    for i in range(len(s)):
        if s[i]==' ':
            sum+=1
        else:
            sum+=number[alpha.index(s[i])]
    print('Case #%d: %d'%(x+1,sum))