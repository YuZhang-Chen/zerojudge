for _ in range(int(input())):
    c=True
    a=input()
    b=input()
    if len(a)!=len(b):
        c=False
    else:
        for i in range(len(a)):
            if a[i]==b[i]:
                continue
            else:
                if a[i] in 'aeiou' and b[i] in 'aeiou':
                    continue
                else:
                    c=False
    if c:
        print('Yes')
    else:
        print('No')