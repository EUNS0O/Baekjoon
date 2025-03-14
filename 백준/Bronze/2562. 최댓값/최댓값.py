list = []
biggest = 0
order = 0
count = 9

while count:
    user = int(input())
    list.append(user)
    count -= 1
    
for i in range(9):
    if list[i] > biggest:
        biggest = list[i]
        order = i

print(biggest)
print(order+1)