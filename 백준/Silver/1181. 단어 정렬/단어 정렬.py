user = []

for i in range(int(input())):
    n = input()
    user.append(n)
    
unique_user = sorted(set(user), key = lambda x: (len(x),x))

for i in unique_user:
    print(i)