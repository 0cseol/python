class AutoMobile:
    neme = ""
    velocity = 0

    def __init__(self, str):    #객체 생성 시 호출되는 특수 내장 함수, self는 객체 자신을 의미
        self.name = str

    def velocityPlus(self):
        self.velocity = self.velocity + 1

    def velocityDw(self):
        self.velocity = self.velocity - 1
        if self.velocity < 0:
            self.velocity = 0

ac = AutoMobile("소나타")
'''문자열 매개변수로 AutoMobile 객체를 생성함
내부적으로는 __init__() 함수를 호출. 매개변수의 문자열은 name 변수의 값으로 대입됨'''
ac.velocity = 20
ac.velocityPlus()
print(ac.name+"의 속도는 %d입니다." %ac.velocity)