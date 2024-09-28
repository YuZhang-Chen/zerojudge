# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:50:49 2022

@author: user
"""

def postorder(p):
    if tree[p]:
        postorder(2*p)
        postorder(2*p+1)
        print(tree[p], end='')

tree=[None]*10001
n=int(input())
s=list(input())
for i in range(len(s)):
    if s[i]=='1':
        s[i]='I'
    else:
        s[i]='B'
for i in range(len(s)):
    tree[len(s)+i]=s[i]

c=len(s)
while c!=1:
    root=[]
    for i in range(c//2):
        a=s.pop(0)
        b=s.pop(0)
        if a!=b or (a=='F' and b=='F'):
            root.append('F')
        elif a=='I' and b=='I':
            root.append('I')
        elif a=='B' and b=='B':
            root.append('B')
    c//=2
    s=root
    for i in range(c):
        tree[c+i]=s[i]
postorder(1)








