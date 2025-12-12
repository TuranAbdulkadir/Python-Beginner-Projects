import time
from turtle import Screen, Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Turtle("turtle")
player.penup()
player.goto(0, -280)
player.setheading(90)

car_manager = []
level = 1

def go_up():
    player.forward(10)

screen.listen()
screen.onkeypress(go_up, "Up")

game_is_on = True
loop_count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Araba üret (Her 6 döngüde bir)
    loop_count += 1
    if loop_count % 6 == 0:
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        car_manager.append(new_car)
    
    # Arabaları hareket ettir
    for car in car_manager:
        car.backward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)
        # Çarpışma kontrolü
        if car.distance(player) < 20:
            game_is_on = False
            player.goto(0,0)
            player.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    # Bitiş çizgisi
    if player.ycor() > 280:
        player.goto(0, -280)
        level += 1
        print(f"Level {level}")

screen.exitonclick()