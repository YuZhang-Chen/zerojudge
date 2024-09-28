# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:50:49 2022

@author: user
"""

for _ in range(int(input())):
    tot=0
    s=list(map(int, input().split()))
    del s[0]
    s.sort()
    if len(s)%2==1:
        num=s[len(s)//2]
    if len(s)%2==0:
        num=(s[len(s)//2]+s[len(s)//2-1])//2
    for i in s:
        tot+=abs(i-num)
    print(tot)