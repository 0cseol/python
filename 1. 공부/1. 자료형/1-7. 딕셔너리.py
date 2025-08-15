''' key 와 value가 한 쌍으로 저장되는 타입
value는 튜플과 다르게 변경 가능 '''

dict = {'번호':10, '성명':'장동건', '나이':23, '사는 곳': '서울'} #딕셔너리 타입 변수 선언
print(dict)
print(type(dict))
print(dict['나이'])         #나이 key 값으로 value값 출력
dict['나이'] = 24             #나이 key 값 항목 변경
print(dict['나이'])
dict['직업'] = '배우'          #직업이라는 key 값과 배우라는 value 항목 추가
print(dict)
print(dict.keys())          #
print(dict.values())
print('사는 곳' in dict)     #key 값 존재 여부 확인
del dict['사는 곳']          #key 값 삭제
print('사는 곳' in dict)
print(dict)