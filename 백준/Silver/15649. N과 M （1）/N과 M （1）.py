
n,m = map(int,input().split())   
arr = [0]*m
isUsed = [False]*(n+1)


def func(k):
    if k == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        if not isUsed[i]:
            arr[k] = i
            isUsed[i] = True
            func(k+1)
            isUsed[i] = False
    
            
func(0)      