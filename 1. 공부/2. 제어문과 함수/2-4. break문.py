''' break문은 반복문을 종료시킴
반복문에 break가 기술되면 반복문의 코드를 실행하지 않고 빠져나옴 '''

#for문과 break문을 이용하여 1에서 20까지 합이 100보다 가장 가깝고 작은 합을 구하시오.
sum, i = 0, 0               #sum, i를 각각 선언
for i in range(1, 20):      #초기값 1부터 19까지 반복(증감 +1 생략)
    sum+= i
    if sum > 100:           #1부터 19까지의 합을 구하다가 100을 넘어서면
        break               #반복문을 빠져나감
sum-= i                     #마지막의 i를 빼기 때문에 100에 도달하기 직전의 합을 구함
print("%d" %sum)
print("----------")

#while문과 break문을 이용하여 입력한 1에서 숫자만큼 합을 구하시오.
sum, i = 0, 0
j = int(input("숫자를 입력합니다."))
while True:
    if i < j:
        i = i + 1
        sum+= i
    elif i == j:            #i와 j가 같아지면
        break               #while문을 빠져나감
print("1에서 %d까지의 합은 %d입니다." %(j, sum))