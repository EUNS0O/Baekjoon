n = int(input())
li = set(map(int,input().split()))

m = int(input())
li2 = list(map(int,input().split()))

def func(arr,arr2):
    for i in arr2:
        if i in arr:
            print(1)
        else:
            print(0)
        
            
func(li,li2)
