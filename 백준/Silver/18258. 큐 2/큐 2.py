import sys
from collections import deque

input = sys.stdin.readline

def main():
    n = int(input())
    queue = deque()
    output = []
    
    for _ in range(n):
        command = input().split()
        
        if command[0] == "push":
            queue.append(command[1])
        elif command[0] == "pop":
            output.append(queue.popleft() if queue else "-1")
        elif command[0] == "size":
            output.append(str(len(queue)))
        elif command[0] == "empty":
            output.append("0" if queue else "1")
        elif command[0] == "front":
            output.append(queue[0] if queue else "-1")
        elif command[0] == "back":
            output.append(queue[-1] if queue else "-1")
    
    sys.stdout.write("\n".join(output))
 
if __name__ == "__main__":
    main()