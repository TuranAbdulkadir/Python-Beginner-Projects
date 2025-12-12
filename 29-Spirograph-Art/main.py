import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Çemberler çizerek dön
for _ in range(72): # 360 dereceyi tamamla
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)

screen = t.Screen()
screen.exitonclick()