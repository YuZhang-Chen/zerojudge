def f(lst):
    new=[]
    for i in range(len(lst)-1):
        new.append(abs(lst[i]-lst[i+1]))
    new.append(abs(s[-1]-s[0]))
    return new

for _ in range(int(input())):
    t=[]
    input()
    s=list(map(int, input().split()))
    t.append(s)
    while 1:
        s=f(s)
        if len(set(s))==1 and s[0]==0:
            print('ZERO')
            break
        elif s in t:
            print('LOOP')
            break
        t.append(s)