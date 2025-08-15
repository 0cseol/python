#숫자 UP & DOWN 게임

import random

count=0
number=random.randint(0,51)
print()
print("정답은","비밀","입니다.")
print()

while True:

    try:
        count=count+1
        guess=int(input("숫자를 입력하세요 : "))
        if guess==number:
            print("                    *정답입니다.",count,"번만에 맞추셨습니다.*")
            break
        elif(number>guess):
            print("                    UP")
            print("                    *",count,"번째 시도입니다.*")
            print()
            print()
        elif(guess>50):
            print("                    *1~50까지의 숫자를 넣어주세요.*")
            print()
            print()
        else:
            print("                    DOWN")
            print("                    *",count,"번째 시도입니다.*")
            print()
            print()
    except:
        print("                    *1~50까지의 숫자를 넣어주세요.*")
        print("                    *",count,"번째 시도입니다.*")
        print()
        print()
print()
print()
print("                * 게  임  이  종  료  되  었  습  니  다. *")
print()
print()
