s=input().strip()
a=''
b=''
for i in range(len(s)):
    if s[i].isalpha():
        a+=s[i]
    if s[i].isdigit():
        b+=s[i]
a=a[::-1]
sum=0
for i in range(len(a)):
    sum+=(ord(a[i])-64)*26**i
print(sum*(int(b)))