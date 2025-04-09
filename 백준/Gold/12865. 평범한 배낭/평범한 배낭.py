import sys

N,K = map(int,sys.stdin.readline().split())

stuff = []
for _ in range(N):                                                         
    W,V = map(int,sys.stdin.readline().split())
    stuff.append((W,V))


stuff.sort(key = lambda x:x[1])
matrix = [[0]*(K+1) for _ in range(len(stuff))]   

if N == 1:
    for i in range(W,K+1):
        matrix[0][i] = V

else:
    for i in range(len(stuff)):
        for j in range(K+1):
            if stuff[i][0] > j: 
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j-stuff[i][0]]+stuff[i][1], matrix[i-1][j])
    #if stuff[i][0]이 [j]보다 크거나 같다면
    #matrix[i][j] = max(matrix[i-1][j-stuff[i][0]]+stuff[i][1], matrix[i-1][j])

print(matrix[len(stuff)-1][K])