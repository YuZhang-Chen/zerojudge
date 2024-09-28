s=input().replace(' ','').lower()
s1=''
for i in s:
    if i.isalpha():
        s1+=i
if 'love' in s1:
    print(0)
else:
    key='abcdefghijklmnopqrstuvwxyz'
    ans=0
    while 1:
        s1=list(s1)
        ans+=1
        for i in range(len(s1)):
            s1[i]=key[(key.index(s1[i])+1)%26]
        s1=''.join(s1)
        if 'love' in s1:
            break
    print(ans)