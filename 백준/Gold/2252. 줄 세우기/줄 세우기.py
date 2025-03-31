import sys
from collections import deque

def topological_sort_bfs(V,graph):
    in_degree = [0] * V  #진입차수 리스트 초기화
    for node in range(V): #진입차수 계산
        for neighbor in graph[node]: #각 노드의 진입차수 계산(노드 간 의존 관계 파악)
            in_degree[neighbor] += 1
            
    queue = deque()
    for i in range(V):
        if in_degree[i] == 0: #진입차수가 0인 것을 큐에 넣어 위상 정렬을 시작할 준비
            queue.append(i) 
             
    
    result = []
    
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1 #진입차수를 줄이는 건 아래에서 함
            if in_degree[neighbor] == 0: #만약 진입차수가 0이라면
                queue.append(neighbor) #큐에 추가
                     
    
    if len(result) == V:
        print(" ".join(str(x+1) for x in result))
    
    else:
        print("Empty")
    

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x1,x2 = map(int, sys.stdin.readline().split())
    graph[x1-1].append(x2-1)
  


topological_sort_bfs(n,graph)