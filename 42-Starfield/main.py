import turtle
import random

stars = []
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)

for _ in range(50):
    star = turtle.Turtle()
    star.color("white")
    star.shape("circle")
    star.shapesize(random.uniform(0.1, 0.5))
    star.penup()
    star.goto(random.randint(-400, 400), random.randint(-300, 300))
    stars.append(star)

while True:
    for star in stars:
        # Yıldızları büyüt ve merkeze çekiyormuş gibi yap
        star.shapesize(star.shapesize()[0] + 0.01)
        
        # Ekrandan çıkarsa sıfırla
        if star.shapesize()[0] > 2:
            star.shapesize(0.1)
            star.goto(random.randint(-400, 400), random.randint(-300, 300))
            
    wn.update()