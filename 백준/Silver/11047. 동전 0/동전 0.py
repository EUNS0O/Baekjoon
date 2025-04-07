import sys

n,k = map(int,sys.stdin.readline().split())
coins = []
for _ in range(n):
    x = int(sys.stdin.readline())
    coins.append(x)

coins.sort(reverse=True)
used_coin = 0

while k>0:
    for i in range(n):
        while k >= coins[i]:
            tmp = k
            used_coin += tmp//coins[i]
            k %= coins[i]
            
            

print(used_coin)
        