import turtle
import math
pantalla = turtle.Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
c1=0
c2=0

def pintalinea(color,largo):

    turtle.speed(1)
    turtle.color(color)
    turtle.pendown
    turtle.forward(largo)
    turtle.penup

def cuadrado(posx,posy):
    turtle.goto(posx,posy)
    pintalinea("red",100)
    turtle.left(90)
    pintalinea("cyan",100)
    turtle.left(90)
    pintalinea("white",100)
    turtle.left(90)
    pintalinea("yellow",100)

for i in range(3):
    turtle.pendown
    print(cuadrado(c1,c2))
    c1+=100
    c2+=100
    turtle.penup

