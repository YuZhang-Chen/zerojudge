s=input().split()
x=s[1]
if x=='/':x='//'
a,b=s[0],s[2]
num=a+x+b
print(eval(num))