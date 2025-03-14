C = int(input())

while C:
    
    user = input()
    score = user.split()
    sum = 0
    persons = int(score[0])
    
    
    
    for i in range(1,len(score)):
        sum = sum + int(score[i])
        
    average = sum/persons
    
    over_average = 0
    under_average = 0
    
    for i in range(1,len(score)):
        if float(score[i]) > average:
            over_average += 1
        elif float(score[i]) <= average :
            under_average += 1
    
    decimal = (over_average/persons)*100
    ratio = round( decimal, 3)
    result = f"{ratio:.3f}" #소수점 세자리까지 표현함
    num = str(result) + "%"
    
    print(num)
    
    C -= 1