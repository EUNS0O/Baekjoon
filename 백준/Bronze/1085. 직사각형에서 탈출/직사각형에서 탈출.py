import math

case = input()
coordinate = list(map(int, case.split()))

x = coordinate[0]
y = coordinate[1]
w = coordinate[2]
h = coordinate[3]

minB = h
minR = w
minT = h
minL = w

for i in range(0,w):
    distance = int(math.sqrt((i-x)**2 + (0-y)**2))
    if distance < minB:
        minB = distance

for i in range(0,h):
    distance = int(math.sqrt((w-x)**2 + (i-y)**2))
    if distance < minR:
        minR = distance
for i in range(0,w):
    distance = int(math.sqrt((i-x)**2 + (h-y)**2))
    if distance < minT:
        minT = distance
for i in range(0,h):
    distance = int(math.sqrt((0-x)**2 + (i-y)**2))
    if distance < minL:
        minL = distance

result = [minB,minR,minT,minL]
if(w>=h):
    shortest = h
else:
    shortest = w 
for i in result:
    if i <= shortest:
        shortest = i
    
print(shortest)