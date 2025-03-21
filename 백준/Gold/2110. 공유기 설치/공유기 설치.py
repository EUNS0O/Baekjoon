n,c = map(int,input().split())
houses=[]

for i in range(n):
    houses.append(int(input()))
 
houses.sort()
start = 1
end = houses[-1] - houses[0]
answer = 0

while start <= end: 
    mid = (start+end)//2
    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] >=  current + mid: #지금 집+설치 간격의 거리보다 같거나 머냐
            count += 1 #설치
            current = houses[i] #지금 위치 업데이트
            
    if count>=c: #설치한 공유기가 목표개수 c개를 넘어 더 넓게 설치할 수 있다는 얘기. 
    
        start = mid + 1 #설치거리 늘리기
        answer = mid #중간 거리
    else: #설치 개수가 총 공유기 개수보다 작을 때(간격을 너무 크게 잡았을 때)
        end = mid - 1 #설치거리 줄이기


print(answer) 