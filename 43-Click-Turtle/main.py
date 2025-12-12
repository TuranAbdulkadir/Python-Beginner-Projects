import turtle
import random

score = 0
wn = turtle.Screen()
wn.bgcolor("lightblue")

target = turtle.Turtle()
target.shape("turtle")
target.color("green")
target.penup()
target.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 24, "bold"))

def clicked(x, y):
    global score
    score += 1
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))
    target.goto(random.randint(-300, 300), random.randint(-250, 250))

target.onclick(clicked)
wn.mainloop()