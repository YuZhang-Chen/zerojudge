def preorder(p):
    if tree[p]!=None:
        print(tree[p], end=' ')
        preorder(p*2+1)
        preorder(p*2+2)

def inorder(p):
    if tree[p]!=None:
        inorder(p*2+1)
        print(tree[p], end=' ')
        inorder(p*2+2)

def postorder(p):
    if tree[p]!=None:
        postorder(p*2+1)
        postorder(p*2+2)
        print(tree[p], end=' ')

tree=[None]*10001
n=int(input())
u,a,b=list(map(int, input().split()))
tree[0]=u
if a!=-1:
    tree[1]=a
if b!=-1:
    tree[2]=b
for _ in range(n-1):
    u,a,b=list(map(int, input().split()))
    if a!=-1:
        tree[tree.index(u)*2+1]=a
    if b!=-1:
        tree[tree.index(u)*2+2]=b

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()