from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bahsini Yap", prompt="Hangi kaplumbağa kazanır? (red/orange/yellow/green/blue/purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Kaplumbağaları başlangıç çizgisine diz
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"KAZANDIN! {winning_color} kaplumbağa birinci oldu! 🏆")
            else:
                print(f"KAYBETTİN! {winning_color} kaplumbağa birinci oldu. 🐢")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()