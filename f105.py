n=int(input())
s=list(map(int, input().split()))
ans=[]
i=2
j=0
stack=[1]

while True:
    if i==n+1:
        break
    if len(stack)==0:
        stack.append(i)
        i+=1
    if stack[-1]==s[j]:
        ans.append(stack.pop())
        if j<n-1:
            j+=1
    else:
        stack.append(i)
        i+=1

while stack:
    if stack[-1]==s[j]:
        ans.append(stack.pop())
        j+=1
    else:
        stack.pop()

print("Yes" if ans==s else "No")