def myfunction01():         #인수 없는 함수 선언. 끝에 colon(:)
    print("함수 선언")       #들여쓰기를 통해 함수 구현 부분 입력
myfunction01()              #함수 호출

def myfunction02(str="인수함수 선언"):  #인수 있는 함수 선언. 기본값 입력
    print(str)                         #인수로 받은 변수를 출력
myfunction02()                         #함수 호출
myfunction02("새로운 인수")             #문자열 인수를 넣어 호출.