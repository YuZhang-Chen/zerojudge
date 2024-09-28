for _ in range(int(input())):
    data=[]
    parent=[]
    parent1=[]
    s=input().split()
    for i in s:
        i=i.split(',')
        a=int(i[0])
        b=int(i[1])
        if a not in parent:
            parent.append(a)
            parent1.append(a)
        if b not in parent:
            parent.append(b)
            parent1.append(b)
        data.append((a,b))

    f=True
    for a,b in data:
        if parent[parent1.index(a)]==parent[parent1.index(b)]:
            f=False
            continue
        mx=max(parent[parent1.index(a)],parent[parent1.index(b)])
        mn=min(parent[parent1.index(a)],parent[parent1.index(b)])
        for i in range(len(parent)):
            if parent[i]==mn:
                parent[i]=mx
    
    if not f:
        print('F')
    else:
        if len(set(parent))==1:
            print('T')
        else:
            print('F')