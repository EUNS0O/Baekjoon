T = int(input())
A = 0
B = 0

while T:
    user = input()
    A,B = map(int,user.split())
    print( A + B )
    T -= 1