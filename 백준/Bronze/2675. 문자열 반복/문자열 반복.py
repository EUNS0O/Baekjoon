for i in range(int(input())):
    user = list(map(str,input().split()))
    
    for r in range(len(user[1])):
        print(user[1][r]*int(user[0]),end="")
    print()
        