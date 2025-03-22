k = int(input())

book = []


for _ in range(k):
    n = int(input())
    
    if n==0:
        book.pop()
    else:
        book.append(n)
        
print(sum(book))