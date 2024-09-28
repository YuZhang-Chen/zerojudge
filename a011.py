from sys import stdin
for s in stdin:
    t=''
    for i in range(len(s)):
        if s[i].isalpha():
            t+=s[i]
        else:
            t+=' '
    t=t.strip()
    t=t.replace(' ',' ')
    t=t.split()
    print(len(t))