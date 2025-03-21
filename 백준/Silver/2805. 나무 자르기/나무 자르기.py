n,m = map(int,input().split())
tree = list(map(int,input().split()))

#어떤 height를 설정.
#만약 나무리스트의 요소가 height보다 크거나 같다면
#나무리스트의 요소들-height를 했을 때의 sum이 m과 같으면 그만.

low, high = 0,max(tree)

while low <= high:
    mid = (low+high)//2
    total = 0
    
    for t in tree:
        if t > mid:
            total += t - mid
            
    if total >= m:
        low = mid + 1
        
    else:
        high = mid - 1 
 


print(high)