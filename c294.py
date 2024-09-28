s=list(map(int, input().split()))
s.sort()
a,b,c=s
print(a,b,c)
if a+b<=c:
    print('No')
elif a*a+b*b<c*c:
    print('Obtuse')
elif a*a+b*b==c*c:
    print('Right')
elif a*a+b*b>c*c:
    print('Acute')