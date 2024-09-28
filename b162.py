dic={}
for _ in range(int(input())):
    n=int(input())
    if n not in dic:
        dic[n]=1
    else:
        dic[n]+=1

for i in sorted(dic.keys()):
    print(i, dic[i])