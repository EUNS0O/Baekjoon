import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
city = [[] for _ in range(n+1)]


for _ in range(m):
    origin, destination, cost = map(int,sys.stdin.readline().split())
    city[origin].append((cost,destination))
    
    
    
def da(graph, start, end, V):
    INF = int(1e9)
    d = [INF]*(V+1)
    d[start] = 0
    que = []
    heapq.heappush(que,(0,start))
    while que:
        w, i = heapq.heappop(que)
        if i == end:
            break
        else:
            if d[i] < w:
                continue
            for cost, neighbor in graph[i]:
                tmp = w + cost
                if tmp < d[neighbor]:
                    d[neighbor] = tmp
                    heapq.heappush(que,(tmp,neighbor))
                    
        
    return d


s, e = map(int,sys.stdin.readline().split())
result = da(city,s,e,n)
total_cost = 0
print(result[e])