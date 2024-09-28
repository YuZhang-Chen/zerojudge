class Node:
    def __init__(self, node):
        self.node = node
        self.nxt = [None]*26

root = Node("root")
node_num = 1

while True:
    try:
        s = input().strip()
        if s == "":
            break
        current = root
        for i in range(len(s)):
            node = s[i]
            idx = ord(node)-65
            if current.nxt[idx] is None:
                node_num += 1
                current.nxt[idx] = Node(node)
            current = current.nxt[idx]
    except:
        break
    
print(node_num)