result = 0

def z(n,r,c):
    global result
   
    if n==2: #변의 길이
        if((r,c)==(0,0)):
            result += 0
        elif (r,c)==(0,1):
            result += 1
        elif (r,c)==(1,0):
            result += 2
        else:
            result += 3
        return    
        

    if r>=(n//2) and c>=(n//2):
        result += int(n*n*3/4)
        return z(n//2,r-n//2,c-n//2)

    elif r>=(n//2) and c<(n//2):
        result += int(n*n*2/4)
        return z(n//2,r-n//2,c)
    
    elif r<(n//2) and c>=(n//2):
        result += int(n*n*1/4)
        return z(n//2,r,c-n//2)
    
    else:
        return z(n//2,r,c)





N,r,c = map(int,input().split())
z(2**N,r,c)
print(result)
