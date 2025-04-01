import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
cal = list(map(int,sys.stdin.readline().split()))

min_result = int(1e9)
max_result = -int(1e9)

def bfs(depth, cal, exp):
    global min_result, max_result
    if depth == n - 1:
        result = num[0]
        for i, op in enumerate(exp):
            if op == 0:
                result += num[i+1]
            elif op == 1:
                result -= num[i+1]
            elif op == 2:
                result *= num[i+1]
            elif op == 3:
                if result < 0:
                    result = -(abs(result)//num[i+1])
                else:
                    result //= num[i+1]
        
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            exp.append(i)
            bfs(depth+1,cal,exp)
            exp.pop()
            cal[i] += 1
        
    

exp = []
bfs(0,cal,exp)

print(max_result)
print(min_result)