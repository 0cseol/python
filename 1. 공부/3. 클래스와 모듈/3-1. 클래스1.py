''' 클래스는 프로그래밍 과정에서
객체를 정의하는 데이터와 이를 활용하는 기능을 가질 수 있는 구조를 의미함
각 클래스는 객체의 상태를 정의할 수 있는 속성(attributes)과
객체의 기능을 정의하는 메서드(methods)를 가질 수 있는 구조
클래스 내의 함수를 메서드라고 부름 '''

class AutoMobile:                                   #클래스 선언
#아래에서 총 2개의 속성, 2개의 메서드 선언

    name = ""                                       #개체의 문자열 속성(attributes) 선언
    velocity = 0                                    #개체의 숫자 속성 선언

    def velocityPlus(self):                         #개체의 기능인 메서드(method) 선언
        self.velocity = self.velocity + 1
        print("속도는 %d입니다." %self.velocity)

    def  velocityDw(self):
        self.velocity = self.velocity - 1
        if self.velocity < 0:
            self.velocity = 0
        print("속도는 %d입니다." %self.velocity)

ac = AutoMobile()       #객체 생성(AutoMobile 클래스를 ac 변수로 접근하여 사용)
ac.velocityPlus()       #메서드 호출
ac.velocity = 20        #객체 속성에 값을 대입
ac.velocityDw()         #메서드 호출

''' 클래스 뒤에 ()가 붙는 것을 "인스턴스를 생성한다"라고 함
위에서 AutoMobile라는 클래스의 인스턴스를 메모리의 한 위치에 생성하고
ac라는 변수가 이를 바인딩 하게 됨
ac.velocty 등은 인스턴스를 통해 함수를 호출하는 과정이다.
self는 객체의 인스턴스 그 자체를 말한다. 즉, 객체 자기 자신을 참조하는 매개변수이다. '''