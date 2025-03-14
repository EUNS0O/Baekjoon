T = int(input())
while T:
    user = input()
    result = []
    score = []
    rate = 0
    
    # 문자열을 한 글자씩 따서 이것을 요소로 갖는 리스트 생성

    for i in range(len(user)):
        if user[i] == 'O':
            result.append('O')
        else:
            result.append('X')

    # 점수로 변환한 리스트 생성
    for i in range(len(result)):
        if result[i] == 'O':
            if i == 0:
                a = 1
                score.append(a)
            else:
                a = score[i-1]+1
                score.append(a)
        else:
            a = 0
            score.append(a)

    for i in range(len(score)):
        rate += score[i]

    print(rate)
    
    T -= 1
    
    
