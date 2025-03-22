t = int(input())


for _ in range(t):
    arr = []
    u = input()
    sum_ = 0
    count = 0
    for i in u:
        count += 1
        if i=='(':
            sum_ += 1
        elif i==')': 
            sum_ -= 1
        
        if sum_ < 0:
            break
            
    if  sum_ == 0 and count==len(u):
        print("YES")
            
    else:
        print("NO")