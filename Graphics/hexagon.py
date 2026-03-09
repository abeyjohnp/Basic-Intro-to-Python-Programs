from turtle import Turtle
import time
def hexagon(t, length):
    t.fillcolor("red")
    t.begin_fill()
    for count in range(6):
       t.forward(length)
       t.left(60)
    t.end_fill()
    time.sleep(5)

t=Turtle()
hexagon(t,100)
