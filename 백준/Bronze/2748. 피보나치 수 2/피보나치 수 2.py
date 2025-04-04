import sys

def fib(n,memo=None):
    if memo is None:
        memo = {}
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

n = int(sys.stdin.readline())
print(fib(n))