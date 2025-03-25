#지금 선택한 값과 탑 배열의 맨 마지막 요소를 비교
#만약 앞의 탑이 지금 탑보다 크다면 len()을 이용해서 인덱스 저장
#만약 앞의 탑이 지금 탑보다 작거나 같다면 ptr를 한 칸 앞으로

n = int(input())
heights = list(map(int,input().split()))

stack = []
result = []

for i in range(n):
    current_height = heights[i]
    
    while stack and stack[-1][0] < current_height:
        stack.pop()
        
    
    if stack:
        result.append(stack[-1][1]+1)
    
    else:
        result.append(0)

    stack.append((current_height, i))
        
print(*result)