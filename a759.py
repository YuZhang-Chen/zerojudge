B=int(input())
cnt=0
lucky=[]
for _ in range(int(input())):
    k,n=input().split()
    k=int(k)
    A=int(n,k)
    if A<B:
        num2=bin(A+B)[2:]
        lucky.append(num2.count('1'))
print(max(lucky),lucky.count(max(lucky)))