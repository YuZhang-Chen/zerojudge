n,t=map(int, input().split())
AND=[]
OR=[]
XOR=[]
lst=[[] for i in range(t)]
for i in range(n):
    s=input().split()
    for j in range(t):
        lst[j].append(s[j])

for i in range(len(lst)):
    if len(set(lst[i]))==1 and lst[i][0]=='1':
        AND.append(1)
    else:
        AND.append(0)
    if '1' in lst[i]:
        OR.append(1)
    else:
        OR.append(0)
    if lst[i].count('1')%2==1:
        XOR.append(1)
    else:
        XOR.append(0)

print('AND:',*AND)
print(' OR:',*OR)
print('XOR:',*XOR)