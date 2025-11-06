import turtle
import math
pantalla = turtle.Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
tortuga = turtle.Turtle()
tortuga.speed(10)
def dibujar_flor(posicion_x, posicion_y, tamaño_flor):
    tortuga.penup()
    tortuga.goto(posicion_x, posicion_y)
    tortuga.pendown() 
    tortuga.color("forestgreen")
    tortuga.setheading(270) # Apuntar hacia abajo
    tortuga.pensize(2)
    tortuga.forward(50)
    tortuga.penup()
    tortuga.goto(posicion_x, posicion_y)
    tortuga.pendown()
    tortuga.color("yellow")
    tortuga.pensize(2)
    for i in range(6):
        tortuga.setheading(i * 72) # 360 / 5 = 72 grados
        tortuga.begin_fill()
        tortuga.circle(tamaño_flor, 60) # Dibuja el arco del pétalo
        tortuga.left(120)
        tortuga.circle(tamaño_flor, 60)
        tortuga.color("yellow")
        tortuga.end_fill()
        tortuga.left(72)
        tortuga.goto(posicion_x, posicion_y + tamaño_flor)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.dot(15)
posiciones = [(-150, 100), (0, 150), (150, 100)]
for x, y in posiciones:    
    dibujar_flor(x, y, 50)  