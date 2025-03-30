import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            
def preorder_traversal(root):
    if root is None:
            return
    print(root.value, end='')
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value, end='')
    inorder_traversal(root.right)
    
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value, end = '')
    
    

n = int(sys.stdin.readline())
g = []
for i in range(n):
    g.append(TreeNode(chr(i+65)))
            

for _ in range(n):
    p,l,r = sys.stdin.readline().split()
    for node in g:
        if node.value == p:
            parent=node
            
    if l!='.':
        for node in g:
            if node.value == l:
               parent.left = node

    elif l=='.':
        parent.left = None

    if r!='.':
        for node in g:
            if node.value == r:
               parent.right = node
               
    elif r=='.':
        parent.right = None
    

preorder_traversal(g[0])
print()
inorder_traversal(g[0])
print()
postorder_traversal(g[0])
            