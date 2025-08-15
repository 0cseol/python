aa = [10, 20, 30, 40]
print("aa[-1]은 %d, aa[-2]는 %d" %(aa[-1],aa[-2]))  #뒤에서부터 첫 번째, 두 번째 요소를 대입
print("----------")

print(aa[0])
print(aa[1])
print(aa[2])
print(aa[3])
print("----------")

print(aa[0 : 2])    #리스트의 범위를 지정하여 출력 첫 번째 부터 두번째까지
print(aa[2 : 4])    #리스트의 세 번째부터 네 번째까지 요소 값 출력
print(aa[0 : 0])
print(aa[0 : ])     #리스트의 첫 번째부터 끝까지 요소 값 출력
print("----------")

print(aa[0 : 0])
print(aa[0 : 1])
print(aa[0 : 2])
print(aa[1 : 1])
print(aa[1 : 2])