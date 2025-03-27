import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))


res = []

if n == 1:
    
    flag = False
    for i in m_list:
        if i == n:
            flag = True
            break
    if flag == True:
        print(1)
    else:
        print(0)
    exit()

for i in m_list:
    left = 0
    right = n-1
    flag = False
        
    while left<=right:
        mid = (left+right)//2
        
        if n_list[mid]==i:
            flag = True
            break
        elif n_list[mid]>i:
            right = mid-1
        else:
            left = mid+1

    if flag == True:
        res.append(1)
    else:
        res.append(0)
            
            
print(' '.join(map(str,res)))