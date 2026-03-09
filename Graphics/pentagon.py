from turtle import *
import time
def pentagon(t, length):
    t.fillcolor("blue")
    t.begin_fill()
    t.forward(length)
    t.left(72)
    time.sleep(1)
    t.forward(length)
    t.left(72)
    time.sleep(1) 
    t.forward(length)
    t.left(72)
    time.sleep(1)
    t.forward(length)
    t.left(72)
    time.sleep(1)
    t.forward(length)
    t.end_fill()
    time.sleep(3)

t = Turtle()
pentagon(t, 100)
