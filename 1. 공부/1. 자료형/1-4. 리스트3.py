aa = []           #요소가 0개인 리스트 변수 선언
aa.append(0)    #값이 0인 요소를 리스트에 추가
aa.append(0)    #append하는대로 요소가 추가됨
aa.append(0)
aa.append(0)
print(len(aa))  #리스트 변수의 크기를 출력(몇 개인지 출력)
print(aa)       #요소의 값들을 출력

bb = []
for i in range(0, 100):  #for문은 제어문 예제에서 참고
    bb.append(i)        #i값을 리스트에 요소로 추가
print(bb)
#for문에 의해 0~99까지 bb리스트에 추가됨. 추가가 모두 완료 된 후 print 동작
