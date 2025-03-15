input()
num = list(map(int, input().split()))
prime = []

for i in num:
    if i == 2 or i == 3:
       prime.append(i)

    elif (i > 1) and (i % 2 != 0) and (i % 3 != 0):
       isPrime = True
       n = (i-1)//2
       for r in range(2,n+1):
         for s in range(2,r+1):
            if ( i == s*r):
                 isPrime=False
       if(isPrime==True):
         prime.append(i) 
            
print(len(prime))   