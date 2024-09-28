n=int(input())
s=list(map(int, input().split()))
idx=int(input())-1 #索引

while 1:
    if idx==0:
        if s[idx+1]<s[idx]:
            idx+=1
        else:
            break
    elif idx==n-1:
        if s[idx-1]<s[idx]:
            idx-=1
        else:
            break
    elif s[idx+1]>s[idx] and s[idx-1]==s[idx]:
        idx-=1
        break
    elif s[idx-1]>s[idx] and s[idx+1]==s[idx]:
        idx+=1
        break
    else:
        l=-1e9
        r=-1e9
        if s[idx-1]<=s[idx]:
            l=s[idx]-s[idx-1]
        if s[idx+1]<=s[idx]:
            r=s[idx]-s[idx+1]
        if l>r:
            idx-=1
        elif l<r:
            idx+=1
    
    if s[idx]<s[idx+1] and s[idx]<s[idx-1]:
        break
print(idx+1)