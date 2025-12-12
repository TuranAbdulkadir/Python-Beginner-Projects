import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "blue", "yellow", "green", "purple", "orange"]

for i in range(200):
    t.color(random.choice(colors))
    t.forward(i * 2)
    t.left(59) # Sihirli açı

wn.exitonclick()