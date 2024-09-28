for _ in range(int(input())):
    stack=[]
    s=input()
    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack!=[]:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        elif i==']':
            if stack!=[]:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    if len(stack)>0:
        print('No')
    else:
        print('Yes')