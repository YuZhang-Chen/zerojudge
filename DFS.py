# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:50:49 2022

@author: user
"""

class list_node:
    def __init__(self):
        self.val=0
        self.next=None

head=[list_node()]*9
run=[0]*9
def dfs(current):
    run[current]=1
    print(current, end=' ')
    ptr=head[current].next
    while ptr!=None:
        if run[ptr.val]==0:
            dfs(ptr.val)
        ptr=ptr.next

data=[[1,2],[2,1],[1,3],[3,1],
      [2,4],[4,2],[2,5],[5,2],
      [3,6],[6,3],[3,7],[7,3],
      [4,8],[8,4],[5,8],[8,5],
      [6,8],[8,6],[8,7],[7,8]]

for i in range(1, 9):
    run[i]=0
    head[i]=list_node()
    head[i].val=i
    head[i].next=None
    ptr=head[i]
    for j in range(20):
        if data[j][0]==i:
            newnode=list_node()
            newnode.val=data[j][1]
            newnode.next=None
            while 1:
                ptr.next=newnode
                ptr=ptr.next
                if ptr.next==None:
                    break

print('圖形的連接串列內容:')
for i in range(1, 9):
    ptr=head[i]
    print('頂點 %d=> '%(i), end='')
    ptr=ptr.next
    while ptr!=None:
        print('[%d] '%(ptr.val), end='')
        ptr=ptr.next
    print()
print('深度優先走訪頂點:')
dfs(1)
print()


















