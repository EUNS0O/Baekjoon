A = int(input())
B = int(input())
C = int(input())

calculate = str(A * B * C)

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

for i in range(len(calculate)):
    if(calculate[i]=='0'):
        zero += 1
    elif(calculate[i]=='1'):
        one += 1
    elif(calculate[i]=='2'):
        two += 1
    elif(calculate[i]=='3'):
        three += 1
    elif(calculate[i]=='4'):
        four += 1
    elif(calculate[i]=='5'):
        five += 1
    elif(calculate[i]=='6'):
        six += 1
    elif(calculate[i]=='7'):
        seven += 1
    elif(calculate[i]=='8'):
        eight += 1
    elif(calculate[i]=='9'):
        nine += 1
        
number=[zero,one,two,three,four,five,six,seven,eight,nine]
num = list(map(int,number))
for i in range(len(number)):
    print(num[i])