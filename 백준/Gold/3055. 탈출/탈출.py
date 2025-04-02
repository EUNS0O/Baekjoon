import sys
from collections import deque

input = sys.stdin.readline

#BFS가 두개 1. 물이 먼저 퍼짐 2. 고슴도치는 물보다 빨리 움직임

R,C = map(int,input().split())
forest = [list(input().strip()) for _ in range(R)]

water_time = [[-1]*C for _ in range(R)] #물이 퍼지는 시간
hedgehog_time = [[-1]*C for _ in range(R)] #고슴도치 이동 시간

water_q = deque()
hog_q = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water_q.append((i,j))
            water_time[i][j] = 0
        elif forest[i][j] == 'S':
            hog_q.append((i,j))
            hedgehog_time[i][j] = 0            

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while water_q:
    x,y = water_q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < R and 0<= ny < C:
            if forest[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                water_q.append((nx, ny))
                

while hog_q:
    x,y = hog_q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C :
            if forest[nx][ny] == 'D':
                print(hedgehog_time[x][y]+1)
                exit()
            if forest[nx][ny] == '.' and hedgehog_time[nx][ny] == -1:
                if water_time[nx][ny] == -1 or hedgehog_time[x][y] + 1< water_time[nx][ny]:
                    hedgehog_time[nx][ny] = hedgehog_time[x][y] + 1
                    hog_q.append((nx, ny))
                    
print("KAKTUS")