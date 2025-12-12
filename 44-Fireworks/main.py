import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)

particles = []
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]

def explode(x, y):
    for _ in range(20):
        p = turtle.Turtle()
        p.shape("circle")
        p.shapesize(0.2)
        p.color(random.choice(colors))
        p.penup()
        p.goto(x, y)
        p.dx = random.randint(-5, 5)
        p.dy = random.randint(-5, 5)
        particles.append(p)

wn.onclick(explode)

while True:
    wn.update()
    for p in particles:
        p.setx(p.xcor() + p.dx)
        p.sety(p.ycor() + p.dy)
        p.dy -= 0.1 # Yerçekimi
        
        if p.ycor() < -300:
            p.clear()
            p.hideturtle()
            particles.remove(p)