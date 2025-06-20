a,b = map(int,input().split())
count = 0

A = set(map(int,input().split()))
B = set(map(int,input().split()))
c = A & B

print(a+b -2*len(c))