from turtle import *

s=Turtle()
a=Screen()
a.bgcolor('green')
s.pencolor('yellow')

a=0
b=0

s.speed(0)
s.penup()
s.goto(0,300)
s.pendown()


while True:
    s.forward(a)
    s.right(b)
    a+=3
    b+=1
    if b==300:
        break
    s.hideturtle()
done()
