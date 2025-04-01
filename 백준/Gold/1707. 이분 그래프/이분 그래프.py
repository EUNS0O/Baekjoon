import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    
    # 양방향 간선 추가
    for _ in range(e):
        u, w = map(int, input().split())
        graph[u].append(w)
        graph[w].append(u)
    
    color = [0] * (v+1)  # 0: 아직 색칠 안됨, 1와 -1: 두 가지 색상
    is_bipartite = True
    
    # 모든 연결 요소를 확인하기 위해 1번부터 v번까지 반복
    for i in range(1, v+1):
        if color[i] == 0:
            # 아직 색칠 안된 정점 i에 대해 BFS 시작
            color[i] = 1
            queue = deque([i])
            while queue and is_bipartite:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # 인접 정점과 색이 같으면 이분 그래프 아님
                        is_bipartite = False
                        break
            if not is_bipartite:
                break
    
    print("YES" if is_bipartite else "NO")
