import sys
n = int(input())

stk = []

def isEmpty(arr):
    if len(arr) == 0:
        return True
    return False


def isSize(arr):
    return len(arr)

for i in range(n):
    
    order = sys.stdin.readline().split()
    
    if order[0] == "push":

        stk.append(order[1])
                
    elif order[0] == "pop":
        if isEmpty(stk)==True:
            print(-1)
             
        else:
            a = stk.pop()
            print(a)
        
    elif order[0] == "size":
        print(isSize(stk))
        
    elif order[0] == "empty":
        if isEmpty(stk)==True:
            print(1)
        else:
            print(0)
        
    elif order[0] == "top":
        if isEmpty(stk)==True:
            print(-1)
            
        else:
            print(stk[-1])