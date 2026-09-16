import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
turtle.speed(1000000000000)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(60):
         t.forward(x)
         t.left(y)
square(100,90)
