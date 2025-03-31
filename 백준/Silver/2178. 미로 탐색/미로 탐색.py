from collections import deque
import sys

                
n,m = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip())for _ in range(n)]

visited = [[False]*m for _ in range(n)]
distance = [[0]*m for _ in range(n)]




def bfs(start_row,start_col):
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    queue = deque([(start_row,start_col)])
    visited[start_row][start_col] = True #방문처리
    distance[start_row][start_col] = 1 #시작 칸
    
    while queue:
            r,c = queue.popleft()
            
            if r== n-1 and c==m-1:
                return distance[r][c]
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr <n and 0 <=nc <m :
                    if graph[nr][nc] == '1' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        distance[nr][nc] = distance[r][c] + 1
                        queue.append((nr,nc))

    return -1



result = bfs(0,0)
print(result)