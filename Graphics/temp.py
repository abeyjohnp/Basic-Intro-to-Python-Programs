from turtle import Turtle
def hexagon(t,length):
    for count in range(6):
        t.forward(length)
        t.left(60)
def radialHexagon(t,n,length):
t= Turtle()
hexagon(t,100)