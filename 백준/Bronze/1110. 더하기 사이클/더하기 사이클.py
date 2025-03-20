

def cycle(num):
    global count
    global new
    
    ten = num//10
    one = num%10

    hap = ten + one

    hap_one = hap%10

    new = (one*10) + hap_one
    count += 1
    
    return new
    
    
N = int(input())
count = 0
new = cycle(N)
 
    
while 1:
    
    if new == N:
        print(count)
        break
        
    cycle(new)