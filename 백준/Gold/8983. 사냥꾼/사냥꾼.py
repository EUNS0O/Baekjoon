m,n,l = map(int,input().split()) 
#m: 사대의 수 n:동물의 수 l:사정거리
m_list = list(map(int,input().split())) #사대 위치

count = 0

for i in range(n):
    x, y = map(int, input().split())
    
    for s in m_list:
        dis = abs(s - x) + y
        
        if dis <= l:
            count +=1
            break
        
print(count)