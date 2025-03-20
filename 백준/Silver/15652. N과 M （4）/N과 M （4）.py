n, m = map(int,input().split())

arr = []

def func(start):
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(start,n+1):
        arr.append(i)
        func(i)
        arr.pop()
        
func(1)