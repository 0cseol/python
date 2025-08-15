aa = [30, 10, 20]
print("현재의 리스트 : %s" % aa)

# 리스트 요소 하나는 정수형으로 인식하지만 리스트 전체는 문자열로 인식함, %s 는 리스트를 대입

aa.append(40)
print("apppend 후의 리스트 : %s" % aa)

aa.pop()  # aa리스트의 제일 마지막 요소를 제거
print("pop 후의 리스트 : %s" % aa)

aa.sort()  # 리스트 요소 값들을 오름차순으로 정렬
print("sort 후의 리스트 : %s" % aa)

aa.reverse()  # 역순으로 정렬
print("reverse 후의 리스트 : %s" % aa)

aa.insert(2, 222)  # aa리스트의 세 번째 위치에 222값을 추가
print("insert 후의 리스트 : %s" % aa)
print("20값의 위치 : %d" % aa.index(20))  # 20이라는 요소 값이 있는 위치 출력(첫번째는 0)

aa.remove(222)  # 222 요소 값 리스트에서 삭제
print("remove(222)후의 리스트 : %s" % aa)

aa.extend([77, 88, 77])  # 리스트를 확장
print("extend[77,88,77])후의 리스트 : %s" % aa)
print("77값의 개수 : %d" % aa.count(77))  # 리스트에서 77 요소 값의 개수 출력
