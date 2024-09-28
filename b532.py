aa=['+','-','*','/','%']
for _ in range(int(input())):
    s=input()
    for i in aa:
        if i in s:
            x=s[s.index(i)]
            s=s.replace(x,' ')
            break
    s=s.split()
    a=s[0]
    b=s[1]
    a1=int(''.join([i for i in a if i.isdigit()]))
    b1=int(''.join([i for i in b if i.isdigit()]))
    ans=''.join([str(a1),x,str(b1)])
    print(int(eval(ans)))