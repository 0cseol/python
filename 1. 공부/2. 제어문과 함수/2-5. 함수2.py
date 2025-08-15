def mydef01():
    i = 10
    j = 20
    print(i + j)
mydef01()

def mydef02(i, j):
    print(i + j)
mydef02(10, 20)

#숫자 두 개와 연산자를 입력하면 계산하는 함수 만들기
def mydef03(i, j, p):       #세 개의 인수를 받는 함수 선언
    if p == '+':
        print(i + j)
    elif p == '-':
        print(i - j)
    elif p == '*':
        print(i * j)
    elif p== '/':
        print(i / j)
n=int(input("첫 번째 숫자를 입력합니다. "))
m=int(input("두 번째 숫자를 입력합니다. "))
p=(input("연산자를 입력하세요(+, -, *, /) "))
mydef03(n, m, p)