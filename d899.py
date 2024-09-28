L,R=map(int, input().split())
s1=''
for i in range(L,R+1):
    s1+=str(i)
print(s1.count('2'))