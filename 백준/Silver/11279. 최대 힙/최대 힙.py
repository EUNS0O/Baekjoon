from queue import PriorityQueue
import sys

que = PriorityQueue()

n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if que.empty():
            print(0)
        else:
            print(-que.get())
    
    else:
        que.put(-x)