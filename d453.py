# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:50:49 2022

@author: user
"""

o=int(input())
for _ in range(o):
    n,m,a,b,x1,x2=map(int, input().split())
    data=[]
    for i in range(n):
        s=input()
        data.append([])
        data[i].append('#')
        for j in range(m):
            if s[j]=='1':
                data[i].append('#')
            else:
                data[i].append(int(s[j]))
        data[i].append('#')
    data.insert(0, ['#']*len(data[0]))
    data.append(['#']*len(data[0]))

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    qx=[b]
    qy=[a]
    data[a][b]=1
    while qy!=[]:
        y=qy.pop(0)
        x=qx.pop(0)
        for i in range(4):
            r=y+dy[i]
            c=x+dx[i]
            if data[r][c]==0:
                data[r][c]=data[y][x]+1
                qy.append(r)
                qx.append(c)

    if data[x1][x2]!='#':
        print(data[x1][x2])
    else:
        print(0)














