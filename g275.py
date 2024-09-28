n=int(input())
for i in range(n):
    ans=''
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    if a[1]==a[3] or a[1]!=a[5] or b[1]==b[3] or b[1]!=b[5]:
        ans+='A'
    if a[-1]==0 or b[-1]==1:
        ans+='B'
    if a[1]==b[1] or a[3]==b[3] or a[5]==b[5]:
        ans+='C'
    
    if ans=='':
        print('None')
    else:
        print(ans)