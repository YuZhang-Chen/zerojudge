alpha='uzrmatifxopnhwvbslekycqjgd'
num='mjqhofawcpnsexdkvgtzblryui'

for _ in range(int(input())):
    s=input().split()
    n=s.pop(0)
    if s[0].isalpha():
        ans=0
        for i in s:
            ans+=alpha.index(i)+1
    else:
        ans=''
        for i in s:
            i=int(i)
            ans+=num[i-1]
    print(ans)