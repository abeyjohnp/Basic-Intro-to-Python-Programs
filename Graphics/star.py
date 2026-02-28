from turtle import Turtle
def star(t,length):
    for i in range(5):
        t.forward(length)
        t.right(144)
t= Turtle()
star(t,100)