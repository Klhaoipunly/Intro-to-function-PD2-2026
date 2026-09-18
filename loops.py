import turtle
from turtle import *
t = Turtle()
t.speed(0)
t.shape('turtle')

#def square():
#   for i in range(4):
#       t.forward(100)
#       t.left(90)

#for i in range(60):
#   square()
#   t.right(5)

#def square(x,y):
   #for i in range(4):
       #t.forward(x)
       #t.right(y)

#def square2():
    #length = 5
    #for i in range(60):
        #square(length,90)
        #t.right(5)
        #length += 5

#square2()

def star(length):
    for i in range(5):
        t.forward(length)
        t.right(144)

def star2():
    length = 10

    for i in range(50):
        star(length)
        t.right(6)
        length +=6

star2()

turtle.done()