key=[]
for i in range(97,123):
    key.append(chr(i))
for i in range(97,123):
    for j in range(i+1,123):
        key.append(chr(i)+chr(j))
for i in range(97,123):
    for j in range(i+1,123):
        for k in range(j+1,123):
            key.append(chr(i)+chr(j)+chr(k))
for i in range(97,123):
    for j in range(i+1,123):
        for k in range(j+1,123):
            for x in range(k+1,123):
                key.append(chr(i)+chr(j)+chr(k)+chr(x))
for i in range(97,123):
    for j in range(i+1,123):
        for k in range(j+1,123):
            for x in range(k+1,123):
                for l in range(x+1,123):
                    key.append(chr(i)+chr(j)+chr(k)+chr(x)+chr(l))

while 1:
    try:
        s=list(input())
        if sorted(s)!=s:
            print(0)
        else:
            print(key.index(''.join(s))+1)
    except:
        break