n = int(input())

li1 = [False for _ in range(20)] #column
li2 = [False for _ in range(50)] #오른쪽 대각선
li3 = [False for _ in range(50)] #왼쪽 대각선
ans =  0

def func(r):
    global ans
    if r==n:
        ans += 1
           
    
    for i in range(n):
        if not li1[i] and not li2[r+i] and not li3[r-i+n-1]:
            li1[i] = True
            li2[r+i] = True
            li3[r-i+n-1] = True
            func(r+1)
            li1[i] = False
            li2[r+i] = False
            li3[r-i+n-1] = False
            
func(0)
print(ans) 