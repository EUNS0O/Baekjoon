n,m = map(int,input().split())
arr = []

def func():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        arr.append(i)
        func()
        arr.pop()

func()