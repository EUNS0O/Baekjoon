import sys


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
stack = [1]
visited = set([1])

while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = node
            stack.append(neighbor)
    
    
for i in range(2, n+1):
    print(parent[i])

    