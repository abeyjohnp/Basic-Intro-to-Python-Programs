from turtle import Turtle
import time
def star(t,length):
    for i in range(5):
        t.forward(length)
        t.right(144)
    time.sleep(4)
t= Turtle()
star(t,100)