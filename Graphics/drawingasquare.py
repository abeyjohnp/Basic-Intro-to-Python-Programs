from turtle import Turtle
import time
def drawSquare(t,x,y,length):
    t.fillcolor("blue")
    t.begin_fill()
    t.up() #lifting the pen up
    t.goto(x,y)
    t.setheading(270)
    t.down() #putting pen down
    t.speed(1) #set speed slow
    for count in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()
    time.sleep(2)
t= Turtle()
drawSquare(t,10,10,260)
