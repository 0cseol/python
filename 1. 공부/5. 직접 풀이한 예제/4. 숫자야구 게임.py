#숫자야구 게임


import random   #랜덤 불러오기
count=0         #count 초기값 0 대입



while True:     #참인 경우일때까지 반복
    number=str(random.randint(0,1000)). zfill(3)    #0~999를 산출(숫자아닌 문자형태로 산출), 세자리 맞춤(빈곳은 왼쪽에 0 대입)
    if number[0]==number[1] or number[1]==number[2] or number[0]==number[2]:    #만일 동일한 숫자가 있으면
        number=str(random.randint(0,1000)). zfill(3)    #위의 코드 재실행(복붙)
    else:
        break   #모든 숫자가 다른 경우 반복 중지

print()
print("정답은","비밀","입니다.")  #정답 number 또는 "비밀" 작성
print()


while True:

    try:    #시도
        count=count+1   #count에 1을 더함
        guess=input("숫자를 입력하세요 : ")     #guess값 선언, input한 값이 guess값이 됨
        if len(guess)!=3:   #guess에 입력한 값의 길이(length)가 3자리가 아니면
            raise           #강제로 에러 생성(except로 이동)

        for i in guess:                 #guess 값의 i번째 문자에 대하여 반복
            if i not in '0123456789':   #모든 입력이 숫자가 아닌 경우
                raise                   #강제로 에러 생성

        if guess[0]==guess[1] or guess[1]==guess[2] or guess[0]==guess[2]:  #guess값에 중복된 값이 있으면
            raise                                                           #강제로 에러 생성
        
        if guess==number:               #guess값이 number와 일치한 경우
            print("                    정답입니다.",count,"번만에 맞추셨습니다.")
            break

        else:                           #if가 아닌 모든 경우
            strike=0                    #strike 선언, 0대입
            ball=0
            answer=list(number)         #answer 선언, answer값을 만들고 number값을 복사(임시변수로 사용)
            for i in range(3):          #i에 대하여 3번 반복
                if guess [i]==number[i]:    #guess와 number값의 세자리가 같은 것이 있다면
                    strike+=1               #strike 값을 하나 올리고
                    answer[i]='s'           #answer의 해당 문자를 s로 치환(ball 선별시 중복되지 않게하기 위함)

            for i in range(3):
                if guess[i] in answer:      #answer의 어디라도 guess값이 있다면(이미 strike는 선별서 치환됨)
                    ball+=1                 #ball의 값을 하나 올리고
                    answer[answer.index(guess[i])]='b'  #guess의 i번째를 answer에서 찾아서(참조하여) b로 바꿔줌


            print("                    틀렸습니다.")     #틀린 값이므로(else에 종속) 다음의 문장 프린트
            print("                    스트라이크: {},  볼: {}".format(strike,ball))  #중괄호 안에 순서대로 대입(format)
            print("                    *",count,"번째 시도입니다.*")
            print()
            print()
    except:
        print("                    *서로 다른 3자리 수를 입력해주세요.*")
        print("                    *",count,"번째 시도입니다.*")
        print()
        print()
print()
print()
print("                * 게  임  이  종  료  되  었  습  니  다. *")
print()
print()
