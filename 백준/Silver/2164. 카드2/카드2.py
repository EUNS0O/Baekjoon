from collections import deque


N = int(input())
queue = deque(range(1,N+1))
if len(queue)==1:
    print(queue[0])
else:
    
    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[0])