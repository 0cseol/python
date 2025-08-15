#반복문 연습
#1부터 10까지 짝수만 합을 구하는 프로그램

sum=0

for i in range(1,11):
    if(i%2==0): #i를 2로 나눈 나머지가 0이라
        sum=sum+i
print(sum)
