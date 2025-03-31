import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
infected = [False]*(n+1)

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
        
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start) 
    
    while queue:
        v = queue.popleft()
        infected[v] = True
        
        for neighbor in graph[v]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)    
                
    
        
bfs(graph,1)
count = 0

for i in range(2,len(infected)):
    if infected[i] == True:
        count += 1
        
print(count)