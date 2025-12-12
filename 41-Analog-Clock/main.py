import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    
    # Saat kolu
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
    
    # Dakika
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)
    
    # Saniye
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.color("red")
    pen.pendown()
    pen.fd(200)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    
    pen.clear()
    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)