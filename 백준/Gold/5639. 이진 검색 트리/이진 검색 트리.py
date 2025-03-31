import sys

sys.setrecursionlimit(5000)

class Node:
    def __init__(self,key):
        
        self.left = None
        self.right = None
        self.value = key 
        

        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root,key)
        
    def _insert_rec(self,node,key):
        if key<node.value:
            if node.left is None:
                node.left = Node(key)
                
            else:
                self._insert_rec(node.left,key)
                
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right,key)
                
    def postorder_traversal(self,root):
        if not root:
            return []
        
        result = [] #순회 결과를 저장할 리스트
        stack = [] #스택을 사용하여 트리를 순회
        current = root #현재 노드를 가리키는 포인터
        while current or stack:
            if current:
                stack.append(current) # 현재 노드를 스택에 넣음
                current = current.left # 왼쪽 자식으로 이동
            else:
                node = stack[-1] # 스택에서 가장 최근에 넣은 노드를 꺼냄
                if node.right and (not result or result[-1] != node.right.value):
                    current = node.right # 오른쪽 자식으로 이동
                else:
                    result.append(node.value) # 현재 노드를 후위 순회 결과에 추가
                    stack.pop() #현재 노드를 스택에서 제거
                    
        for i in result:
            print(i,end = "\n")
   
bst = BST()

tree = map(int,sys.stdin.read().splitlines())
for i in tree:
    bst.insert(i)
    
if bst.root:
    bst.postorder_traversal(bst.root)