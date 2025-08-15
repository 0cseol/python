''' 튜플은 리스트와 비슷하지만 요소값 변경 불가능
읽기전용이라고 생각할 수 있음 '''

str="문자열"        #문자열 변수 선언
print(str[0])       #첫 번째 자리의 문자 출력
print(str[-1])      #뒤에서 첫 번째 자리 문자 출력
#str[-1]='렬'       #문자 수정시 에러 발생
card='red', 4, 'python', True   #card 튜플 선언
print(card)
print(card[1])                  #튜플의 첫 번째 요소 출력
#card[0]='blue'                 #요소 수정시 에러 발생