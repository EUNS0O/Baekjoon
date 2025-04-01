import sys
from collections import deque

def bfs(graph, start):
    distances = [-1]*len(graph)
    distances[start] = 0
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
                
    return distances

n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    

result = bfs(graph,x)
count = 0

for i in range(len(result)):
    if result[i] == k:
        print(i)
        count +=1
        
    if i == len(result)-1 and count==0:
        print(-1)