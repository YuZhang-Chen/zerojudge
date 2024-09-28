a='0'+input()
b='0'+input()
t=int(input())
lcs=[]
for i in range(len(a)):
    lcs.append([])
    for j in range(len(b)):
        lcs[i].append(0)

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i]==b[j]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])

num=lcs[-1][-1]
if num<t:
    print('sitini na tisa')
else:
    print('kwa nini unaendesha')