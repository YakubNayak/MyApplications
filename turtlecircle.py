from turtle import *

s=Turtle()
a=Screen()
a.bgcolor('pink')
s.pencolor('red')

a=0
b=0

s.speed(0)
s.penup()
s.goto(0,200)
s.pendown()


while True:
    s.forward(a)
    s.right(b)
    a+=3
    b+=1
    if b==240:
        break
    s.hideturtle()
done()
