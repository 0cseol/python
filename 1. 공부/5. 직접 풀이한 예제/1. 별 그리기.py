#별 그리기

import turtle as t
t.pensize(1)
t.speed(10)
y=0

def star(x,color):
        t.penup()
        t.color(color)
        t.goto(-x/2,x/5)
        t.pendown()
        t.begin_fill()
        for i in range(0,5):
            t.fd(x)
            t.right(144)
        t.end_fill()

def star2(x):
        while True:
                if x>51:
                        star(x,'red')
                else:
                        break
                if x-50>51:
                        star(x-50,'blue')
                else:
                        break
                if x-100>51:
                        star(x-100,'yellow')
                else:
                        break

def star3(x):
        while True:
                if x<51:
                        break
                else:
                        star2(x)
                        star2(x-150)
                        x=x-300


t.bgcolor('green')

star3(500)
