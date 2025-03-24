m,n,l = map(int,input().split()) 
#m: 사대의 수 n:동물의 수 l:사정거리
m_list = list(map(int,input().split())) #사대 위치
m_list.sort()

count = 0
for _ in range(n):
    x, y = map(int,input().split())
    left = 0
    right = m-1
    
    while left<=right:
        
        mid = (left + right)//2
        dis = abs(m_list[mid]-x)+y
        
        if dis <= l:
            count += 1
            break    
        elif x < m_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
print(count)
