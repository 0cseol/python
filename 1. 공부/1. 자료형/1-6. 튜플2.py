str="파이썬문자열"
print(str[0])
print(str[-1])
#str[-1]='렬'                   #수정시 에러 발생하므로 주석처리함
'''문자열은 튜플 타입 변수로 선언이 되므로 수정시 에러 발생
튜플은 한 번 선언된 값 변경 불가능 '''

card='red', 4, 'python', True   #다양한 타입의 card 튜플 선언
print(card)
print(card[1])
print(card[2])
print(card[3])
#card[0]='blue'                 #수정시 에러 발생하므로 주석처리함