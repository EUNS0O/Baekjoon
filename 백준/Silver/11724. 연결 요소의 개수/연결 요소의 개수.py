import sys

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [False]*n
count = 0

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

def stack_dfs(v,graph):
    global visited
    stack = [v]
    while stack:
        x = stack.pop()
        if visited[x] == False:
            visited[x] = True
            
            for i in graph[x]:
                if visited[i] == False:
                    stack.append(i)
    
    
    
        
for i in range(n):
    if visited[i] == False:
        
        stack_dfs(i,graph)
        count += 1
        
print(count)