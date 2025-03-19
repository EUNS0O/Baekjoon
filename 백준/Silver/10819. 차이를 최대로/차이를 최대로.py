from itertools import permutations
 
N = int(input())

num = list(map(int,input().split()))
sum_list = []

for comb in permutations(num,N):
    sum_ = 0
    for i in range(N-1):
        sum_ += abs(comb[i+1] - comb[i])
        
    sum_list.append(sum_)
    
print(max(sum_list))
