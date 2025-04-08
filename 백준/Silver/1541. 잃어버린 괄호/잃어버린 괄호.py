import sys

u = sys.stdin.readline().strip()
stack = []
for i in u:
    if i != '-' and i !='+':
        stack.append(int(i))
    else:
        stack.append(i)

mul = 1
temp = 0
total = 0

while stack:
    x = stack.pop()
    if x =='-':
        total -= temp
        temp = 0
        mul = 1
      
    elif x =='+':
        mul = 1
        
    else:
        temp += x*mul
        mul *= 10   
        
total += temp

print(total)
    
    