import turtle
import random

# Configuración inicial de la pantalla
pantalla = turtle.Screen()
pantalla.title("Carrera de Tortugas")
pantalla.bgcolor("#333333")

# Función para crear una tortuga con un color aleatorio
def crear_tortuga(color):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(color)
    tortuga.penup()
    return tortuga

# Crear y posicionar las tortugas
num_tortugas = 5
colores = ["red", "blue", "green", "orange", "purple"]
tortugas = [crear_tortuga(color) for color in colores]
espaciado_vertical = 100

for i, tortuga in enumerate(tortugas):
    tortuga.goto(-200, espaciado_vertical * (i - (num_tortugas - 1) / 2))

# Dibujar línea de inicio y meta
linea_inicio = turtle.Turtle()
linea_inicio.color("white")
linea_inicio.penup()
linea_inicio.goto(-200, 250)
linea_inicio.pendown()
linea_inicio.goto(-200, -250)
linea_inicio.hideturtle()

linea_meta = turtle.Turtle()
linea_meta.color("white")
linea_meta.penup()
linea_meta.goto(270, 250)
linea_meta.pendown()
linea_meta.goto(270, -250)
linea_meta.hideturtle()


# Realiza la carrera
while any(tortuga.xcor() < 200 for tortuga in tortugas):
    for tortuga in tortugas:
        avance = random.randint(1, 10)
        tortuga.forward(avance)

# Encuentra la tortuga ganadora
ganadora = max(tortugas, key=lambda tortuga: tortuga.xcor())
indice_ganadora = tortugas.index(ganadora)

# Muentra el resultado
mensaje = turtle.Turtle()
mensaje.color("white")
mensaje.penup()
mensaje.hideturtle()
mensaje.goto(0, 0)
mensaje.write("¡La Tortuga {} gana la carrera! 🏆".format(indice_ganadora + 1), align="center", font=("Arial", 30, "bold"))

# Cerrar la pantalla al hacer clic
pantalla.exitonclick()
