class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None

def create_tree(root,val):
    newnode=tree()
    newnode.data=val
    newnode.left=None
    newnode.right=None
    if root==None:
        root=newnode
        return root
    else:
        current=root
        while current!=None:
            backup=current
            if current.data>val:
                current=current.left
            else:
                current=current.right
        if backup.data>val:
            backup.left=newnode
        else:
            backup.right=newnode
    return root

def preorder(ptr):
    if ptr!=None:
        print(ptr.data, end=' ')
        preorder(ptr.left)
        preorder(ptr.right)

while 1:
    try:
        n=int(input())
        s=list(map(int, input().split()))
        ptr=None
        for i in range(n):
            ptr=create_tree(ptr, s[i])
        preorder(ptr)
        print()
    except:
        break