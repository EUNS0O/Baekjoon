import sys
import heapq

n = int(sys.stdin.readline())
intervals =[]
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a>b:
        a,b= b,a
    
    intervals.append((a,b))
    
d = int(sys.stdin.readline())

intervals = [(a,b)for a,b in intervals if b-a<=d]
intervals.sort(key=lambda x:x[1])

heap = []
max_count = 0

for a,b in intervals:
    heapq.heappush(heap,a)
    
    while heap and b - heap[0] >d:
        heapq.heappop(heap)
        
    max_count = max(max_count, len(heap))
    
print(max_count)
