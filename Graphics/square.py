from turtle import Turtle
import time
def square(t, length):
    for count in range(4):
       t.forward(length)
       t.left(90)
    time.sleep(4)

t=Turtle()
square(t,100)