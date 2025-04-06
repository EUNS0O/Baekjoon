import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    cost = int(sys.stdin.readline())
    
    dp = [0]*(cost+1)
    dp[0] = 1#인덱스 값을 만들 수 있는 가짓수 저장
    for coin in coins:
        for money in range(cost+1):
            if money>=coin: 
                dp[money] += dp[money-coin]

    print(dp[cost])