a='0'+input()
b='0'+input()
ans=''
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i]==b[j] and a[i] not in ans:
            ans+=a[i]
if ans=='':
    print('E')
else:
    print(ans)