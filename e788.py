lst=[]
for _ in range(int(input())):
    number, name=input().split()
    lst.append((number[0], number[-1], name))

lst.sort(key=lambda x:(x[1], x[0]))
for i in lst:
    print(*i[1:], sep=": ")