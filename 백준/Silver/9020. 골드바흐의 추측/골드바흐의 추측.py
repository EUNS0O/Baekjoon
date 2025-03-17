def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True


for o in range(int(input())):
    x = int(input())
    a = x//2
    b = x//2
    while 1:
        if isPrime(a) == True and isPrime(b) == True:
            print(b, a)
            break
        else:
            a += 1
            b -= 1