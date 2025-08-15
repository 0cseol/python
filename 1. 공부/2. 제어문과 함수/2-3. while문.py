''' 조건부 반복문. 조건이 True일 때 실행되며, 조건이 False가 될 때까지 반복됨
조건이 False가 되지 않으면 무한루프 발생 '''

str = "hello"
i = 0
while i < 3:
    print(str)
    i = i + 1
print("----------")

#while문으로 입력한 숫자만큼str을 반복 출력하시오.
i = int(input("반복 횟수를 입력합니다."))
j = 1
k = True            #k 값을 True로 지정
while k:            #k에 대하여 while문 실행(True에서 반복)
    j = j + 1
    if i < j:
        k = False   #조건이 맞을 때 False를 대입
    print(str)