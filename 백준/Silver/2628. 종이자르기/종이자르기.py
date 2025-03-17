r,c = map(int,input().split()) #가로 길이, 세로 길이
x = [0,r]
y = [0,c]
for i in range(int(input())):
    a,b = map(int,input().split())
    if a == 0:
        y.append(b)
    else:
        x.append(b)

x.sort()
y.sort()

maxX = 0
maxY = 0 

for q in range(1,len(x)):
    maxX = max(maxX, x[q]-x[q-1])
       
for w in range(1,len(y)):
    maxY = max(maxY, y[w]-y[w-1])

print(maxX*maxY)