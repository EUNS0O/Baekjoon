n,m = map(int,input().split())

arr=[0]*(m) #최대 m개이니까
isUsed = [False]*(n+1) #숫자의 상태를 직관적으로 알기 위해(1부터 n까지)

def func(k):
    if k==m:
        for i in range(m-1):
            if arr[i]>=arr[i+1]:
                return
        else:
        
            print(' '.join(map(str,arr)))
            return 
        
    for i in range(1,n+1):
        if isUsed[i]==False:
            arr[k]=i
            isUsed[i]=True
            func(k+1)
            isUsed[i]=False


func(0)
