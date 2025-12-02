
import turtle
import random
import math

# ---------- Configuración de la pantalla ----------
screen = turtle.Screen()
screen.setup(width=1100, height=750)
screen.title("Flores azules para Andrea ❤")
screen.tracer(0)  # desactiva actualizaciones automáticas para dibujar más rápido

# ---------- Fondo tipo césped ----------
def draw_grass_background(color="#cfeeb0", blade_color="#7db96f", density=220):
    """
    Dibuja fondo verde (césped) y unas briznas (líneas) para textura.
    - color: color base del césped (más claro)
    - blade_color: color de las briznas
    - density: número aproximado de briznas
    """
    bg = turtle.Turtle()
    bg.hideturtle()
    bg.speed(0)
    bg.penup()
    # rectángulo de fondo (cubre toda la ventana)
    w = screen.window_width()
    h = screen.window_height()
    bg.goto(-w/2, -h/2)
    bg.color(color)
    bg.begin_fill()
    bg.pendown()
    for _ in range(2):
        bg.forward(w)
        bg.left(90)
        bg.forward(h)
        bg.left(90)
    bg.end_fill()
    bg.penup()

    # dibujar briznas de hierba por encima, en la mitad y parte inferior del canvas
    blade = turtle.Turtle()
    blade.hideturtle()
    blade.speed(0)
    blade.color(blade_color)
    blade.pensize(2)
    min_x = -w/2 - 20
    max_x = w/2 + 20
    # repartimos las briznas a lo ancho pero concentradas en la mitad / baja del lienzo
    for i in range(density):
        x = random.uniform(min_x, max_x)
        # y más probable en la mitad/parte inferior para que no tape flores altas
        y = random.uniform(-h/2, h/8)
        blade.penup()
        blade.goto(x, y)
        blade.setheading(random.uniform(80, 100))  # ligeramente vertical
        blade.pendown()
        blade.forward(random.uniform(12, 36))
    blade.penup()

# ---------- Flor (corrección para centro bien centrado) ----------
def draw_flower(x, y, petal_count=6, petal_radius=40, petal_angle=60, scale=1.0,
                petal_outline="#083d77", petal_fill="#6fa8ff",
                center_fill="#ffd43b", stem_color="#1f8a3d"):
    """
    Dibuja una flor con centro exactamente en (x,y).
    - Para centrar correctamente, los pétalos se dibujan alrededor de (x,y)
      sin desplazar el círculo central: así el centro es siempre (x,y).
    """
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    angle_step = 360.0 / petal_count
    # Dibujar cada pétalo tomando el punto (x,y) como centro de referencia.
    # Para formar un pétalo usamos arcos, pero nos aseguramos de regresar al centro.
    for i in range(petal_count):
        theta = math.radians(i * angle_step)  # ángulo del pétalo en radianes
        # posición de inicio del arco: desplazamos ligeramente desde el centro hacia afuera
        offset = petal_radius * 0.28 * scale
        start_x = x + math.cos(theta) * offset
        start_y = y + math.sin(theta) * offset

        pen.penup()
        pen.goto(start_x, start_y)
        # orientar perpendicular al radio para que el pétalo "salga" radialmente
        heading = math.degrees(theta) + 90 - (petal_angle / 2)
        pen.setheading(heading)
        pen.pendown()
        pen.color(petal_outline, petal_fill)
        pen.begin_fill()
        # primer arco
        pen.circle(petal_radius * scale, petal_angle)
        # volver por el otro arco
        pen.left(180 - petal_angle)
        pen.circle(petal_radius * scale, petal_angle)
        pen.end_fill()
        pen.penup()

    # CENTRO de la flor: dibujado exactamente en (x,y) -> ahora sí queda centrado.
    pen.goto(x, y - 12 * scale)  # el y-12 solo baja el círculo para que se vea "encajado", pero sigue centrado en x
    pen.setheading(0)
    pen.pendown()
    pen.color("black", center_fill)
    pen.begin_fill()
    pen.circle(12 * scale)
    pen.end_fill()
    pen.penup()

    # tallo: empezamos en la parte inferior del centro (x, y - petal_radius*scale)
    stem_start_x = x
    stem_start_y = y - petal_radius * scale
    pen.goto(stem_start_x, stem_start_y)
    pen.setheading(-90)
    pen.pendown()
    pen.color(stem_color)
    pen.pensize(max(2, int(6 * scale)))
    pen.forward(80 * scale)

    # hoja simple en el tallo (un poco desplazada)
    pen.right(45)
    pen.color(stem_color, stem_color)
    pen.begin_fill()
    pen.circle(20 * scale, 90)
    pen.left(90)
    pen.circle(20 * scale, 90)
    pen.end_fill()

    pen.penup()
    pen.hideturtle()

# ---------- Corazón y nombre (sin afectar el centro) ----------
def draw_heart(x, y, size=1.0):
    h = turtle.Turtle()
    h.hideturtle()
    h.speed(0)
    h.penup()
    h.goto(x, y)
    h.pendown()
    h.color("red", "#ff6b6b")
    h.begin_fill()
    h.setheading(140)
    h.forward(112 * size)
    for _ in range(200):
        h.right(1)
        h.forward(0.6 * size)
    h.left(120)
    for _ in range(200):
        h.right(1)
        h.forward(0.6 * size)
    h.forward(112 * size)
    h.end_fill()
    h.penup()
    h.hideturtle()
    h.setheading(0)

def write_name(text, x, y, size=56, fontname="Segoe Script"):
    w = turtle.Turtle()
    w.hideturtle()
    w.penup()
    w.goto(x, y)
    w.color("#0b2d8a")
    try:
        w.write(text, font=(fontname, size, "bold"))
    except Exception:
        w.write(text, font=("Arial", size, "bold"))
    w.penup()
    w.hideturtle()

# ---------- MAIN ----------
def main():
    # Fondo tipo césped
    draw_grass_background(color="#cfeeb0", blade_color="#7db96f", density=300)

    # Posiciones y tamaños de las flores (centradas)
    flowers = [
        (-360, 140, 7, 40, 60, 0.95),
        (-200, 80, 7, 36, 60, 0.85),
        (-40, 180, 8, 44, 60, 1.05),
        (120, 120, 7, 38, 60, 0.9),
        (280, 160, 6, 34, 60, 0.9),
    ]
    for x, y, pc, pr, pa, sc in flowers:
        draw_flower(x, y, petal_count=pc, petal_radius=pr, petal_angle=pa, scale=sc)

    # Flor central grande
    draw_flower(0, -20, petal_count=8, petal_radius=72, petal_angle=60, scale=1.0)

    # Corazón a la derecha
    draw_heart(360, -40, size=1.1)

    # Nombre
    write_name("andrea", -120, -260, size=60)

    screen.update()  # actualizar todo lo dibujado
    screen.mainloop()

if __name__ == "__main__":
    main()
