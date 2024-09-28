a='0'+input()
b='0'+input()

c=[]
for i in range(len(a)):
    c.append([])
    for j in range(len(b)):
        c[i].append(0)

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i]==b[j]:
            c[i][j]=c[i-1][j-1]+1
        else:
            c[i][j]=max(c[i-1][j],c[i][j-1],c[i][j])
            
print(c[-1][-1])