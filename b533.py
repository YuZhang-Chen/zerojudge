for _ in range(int(input())):
    s=input().replace('{',' ').replace('}',' }').replace(',','').split()
    A=set()
    B=set()
    c=0
    for i in range(len(s)):
        if s[i]=='}':
            c+=1
        elif c==0:
            A.add(s[i]) 
        else:
            B.add(s[i])
    ans1=list(sorted(A|B))
    ans2=list(sorted(A&B))
    ans3=list(sorted(A-B))
    ans4=list(sorted(A^B))

    ans=''
    if ans1!=[]:
        ans+=str(ans1).replace('[','{').replace(']','}').replace("'",'')
    else:
        ans+='N'
    ans+=', '

    if ans2!=[]:
        ans+=str(ans2).replace('[','{').replace(']','}').replace("'",'')
    else:
        ans+='N'
    ans+=', '

    if ans3!=[]:
        ans+=str(ans3).replace('[','{').replace(']','}').replace("'",'')
    else:
        ans+='N'
    ans+=', '

    if ans4!=[]:
        ans+=str(ans4).replace('[','{').replace(']','}').replace("'",'')
    else:
        ans+='N'
    
    print(ans)