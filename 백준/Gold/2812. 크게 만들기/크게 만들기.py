def solve(n,k,num_str):
    stack = []
    to_remove = k
    
    for num in num_str:
        while to_remove > 0 and stack and stack[-1]<num:
            stack.pop()
            to_remove -= 1
        stack.append(num)
        
    return ''.join(stack[:n-k])

def main():
    n, k = map(int, input().split())
    num_str = input().strip()
    
    print(solve(n,k,num_str))
    
    
if __name__ == "__main__":
    main()