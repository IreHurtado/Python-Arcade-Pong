"""Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los
controles del usuario para las paletas de los jugadores izquierda y derecha."""

import turtle
ventana = turtle.Screen()
ventana.title("Pong en Python")
ventana.bgcolor("pink")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Pelota
pelota=turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("red")
pelota.penup()
pelota.goto(0,0)
pelota.mx = 0.4
pelota.my= 0.4

#Puntaje
puntaje_a= 0
puntaje_b =0

#Contador cont
cont = turtle.Turtle()
cont.speed(0)
cont.color("white")
cont.penup()
cont.hideturtle()
cont.goto(0,265)
cont.write("P1: 0    P2: 0", align="center", font=("Arial", 16, "bold"))

#Funciones para que se muevan los paddles

def paddlea_arriba():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddlea_abajo():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddleb_arriba():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddleb_abajo():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Vinculamos con el teclado

ventana.listen()
ventana.onkeypress(paddlea_arriba, "w")
ventana.onkeypress(paddlea_abajo, "s")
ventana.onkeypress(paddleb_arriba, "Up")
ventana.onkeypress(paddleb_abajo, "Down")


#Loop principal
while True:
    ventana.update()


#Movimiento de pelota

    pelota.setx(pelota.xcor()+pelota.mx)
    pelota.sety(pelota.ycor()+pelota.my)

#Definir bordes de la ventana

    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.my *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.my *= -1

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.mx *= -1
        puntaje_a += 1
        cont.clear()
        cont.write("P1: {}    P2: {}".format(puntaje_a, puntaje_b), align="center", font=("Arial", 16, "bold"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.mx *= -1
        puntaje_b += 1
        cont.clear()
        cont.write("P1: {}    P2: {}".format(puntaje_a, puntaje_b), align="center", font=("Arial", 16, "bold"))

#Choque de pelota y paddle

    if pelota.xcor() < -340 and pelota.ycor() < paddle_a.ycor() + 50 and pelota.ycor() > paddle_a.ycor() - 50:
        pelota.mx *= -1

    if pelota.xcor() < 340 and pelota.ycor() < paddle_b.ycor() + 50 and pelota.ycor() > paddle_b.ycor() - 50:
        pelota.mx *= -1