a,b=input().split()
A=0
B=0
a=a[::-1]
b=b[::-1]
for i in range(len(a)):
    A+=(ord(a[i])-64)*26**i
for i in range(len(b)):
    B+=(ord(b[i])-64)*26**i
print(abs(A-B)+1)