#for문을 이용하여 1에서 10까지의 합을 구하시오.
sum = 0
for i in range(1, 11, 1):
    sum+= i                      #sum에 더함 i를
print("sum : %d" %sum)          #sum값을 출력
print("----------")

#for문을 이용하여 1에서 10까지 식과 합을 구하시오.
sum = 0
for j in range(1,11,1):
    if j < 10:
        print("%d + "%j, end="")    #end는 출력후 줄바꿈하지 않음
    elif j == 10:                   #같은지 판단할때는 등호가 두개(==)
        print("%d = "%j, end="")
    sum+= j
print("%d" %sum)