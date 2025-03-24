
def divide_conquer(x_start,y_start,size,area):
    global white
    global blue
    
    color = area[x_start][y_start]
    
    for i in range(x_start, x_start+size):
        for j in range(y_start,y_start+size):
            if area[i][j] != color:
                
                half_size = size//2
             
                divide_conquer(x_start,y_start,half_size,area)
                divide_conquer(x_start,y_start+half_size,half_size,area)
                divide_conquer(x_start+half_size, y_start, half_size,  area)
                divide_conquer(x_start+half_size,y_start+half_size,half_size,area)
                return
                
    if color==0:
        white += 1
    else:
        blue += 1
                    

    
 
n = int(input()) #한 변의 길이
whole_area = [list(map(int,input().split()))for _ in range(n)]

white = 0
blue = 0

divide_conquer(0,0,n, whole_area)

print(white)
print(blue)
        