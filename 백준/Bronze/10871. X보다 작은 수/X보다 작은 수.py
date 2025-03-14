user = input()
N,X = map(int,user.split())
a = input()
b = a.split()
small = []
c=[]
for i in range(len(b)):
    temp = int(b[i])
    c.append(temp)
    
for i in range(len(c)):
    if(c[i]<X):
        small.append(c[i])

for i in range(len(small)):
    print(small[i],end=" ")