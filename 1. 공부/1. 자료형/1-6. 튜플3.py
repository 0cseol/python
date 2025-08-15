one='하나'
print(type(one))
one="원"            #문자열 전체를 변경
print(one)
two='둘'
print(type(two))
#two[0]='투'        #수정시 에러 발생하므로 주석처리함
print(two[0])
'''전체 변경은 가능하지만 위치 값으로 리턴받은
문자값은 튜플 타입이 되므로 수정 불가'''