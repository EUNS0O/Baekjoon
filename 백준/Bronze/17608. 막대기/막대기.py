import sys
input = sys.stdin.readline
n = int(input())
stick = []

for _ in range(n):
    stick.append(int(input()))    
    
count = 1
m = stick[-1]

for i in range(n-2,-1,-1):
    if stick[i]>m:
        m = stick[i]
        count += 1
        
        
print(count)