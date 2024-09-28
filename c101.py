while 1:
    try:
        dic={}
        c=True
        cc=True
        while 1:
            s=input()
            if s[-2:]=='()':
                c=False
            s=s.replace('(','').replace(')','').split()
            for i in s:
                i=i.split(',')
                key=i[1]
                node=i[0]
                if key in dic:
                    cc=False
                    break
                if key=='':
                    dic['root']=node
                else:
                    dic[key]=node
            if not c:
                break
        ans=[]
        q=['']
        L=''
        R=''
        if 'root' in dic:
            ans.append(dic['root'])
            del dic['root']
        else:
            cc=False

        while len(q)>0:
            node=q.pop(0)
            L=node+'L'
            R=node+'R'
            if L in dic:
                q.append(L)
                ans.append(dic[L])
                del dic[L]
            if R in dic:
                q.append(R)
                ans.append(dic[R])
                del dic[R]
        if not cc:
            print('not complete')
        elif len(dic)>0:
            print('not complete')
        else:
            print(*ans)
    except:
        break