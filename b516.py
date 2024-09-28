alpha=[chr(i) for i in range(97,123)]
alpha1=[chr(i) for i in range(65,91)]
n=int(input())
for i in range(n):
    s=input()
    for i in s:
        if i.isupper():
            print(alpha1[(alpha1.index(i)+3)%26], end='')
        else:
            print(alpha[(alpha.index(i)+3)%26],end='')
    print()