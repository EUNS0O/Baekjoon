from collections import deque

n,k = map(int,input().split())

people = deque(range(1,n+1))
count = 0
li = []

while count!=n:
    for _ in range(1,k):
        x=people.popleft()
        people.append(x)
    a = people.popleft()
    li.append(a)
    count += 1

print("<"+", ".join(map(str,li))+">")