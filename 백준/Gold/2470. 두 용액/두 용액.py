n = int(input())
arr = list(map(int,input().split()))
arr.sort()

pl = 0
pr = n-1
best_res = float('inf')

left = arr[pl]
right = arr[pr]
best_pair = (0,0)

while pl<pr:
    sum_ = arr[pl] + arr[pr]
    
    if abs(sum_) < best_res:
        best_res = abs(sum_)
        best_pair = (arr[pl],arr[pr])
        
    if sum_ == 0:
        break
       
    elif sum_ < 0:
        pl += 1
    
    else:
        pr -= 1
        
    
print(best_pair[0], best_pair[1])