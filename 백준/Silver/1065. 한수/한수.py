n = int(input())

if n<100: 
    print(n)
    
else:
    count =99
    for i in range(100,n+1):
        li = list(map(int,str(i)))
        if((li[2]-li[1]) == (li[1]-li[0])):
            count +=1
    print(count)