import sys

coins = [5,2]
n = int(sys.stdin.readline())
money_list = []
for i in range(n+1):
    money_list.append(i)
dp = [0]*(n+1) 
count = 0
  
for i in range(len(money_list)):
    if 5<=money_list[i] :
        if (money_list[i]%5)%2!=0:
            dp[i] = (money_list[i]//5)-1
            money_list[i] = money_list[i]-((money_list[i]//5)-1)*5
            count += dp[i]
        else:
            dp[i] = money_list[i]//5
            money_list[i] %= 5
            count += dp[i]
            
for i in range(len(money_list)):
    if 2<=money_list[i]:
        
        dp[i] += money_list[i]//2
        money_list[i] %= 2
    

if money_list[n] != 0:
    print(-1)
else:
    print(dp[n])