import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space War")

# Oyuncu
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.setheading(90)
player.goto(0, -250)

# Düşman
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.goto(-200, 250)
enemy_speed = 2

# Mermi
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.hideturtle()
bullet.shapesize(0.5, 0.5)
bullet_state = "ready"

def move_left():
    x = player.xcor()
    if x > -280: player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280: player.setx(x + 20)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

while True:
    wn.update()
    
    # Düşman hareketi
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)
    
    if enemy.xcor() > 280 or enemy.xcor() < -280:
        enemy_speed *= -1
        enemy.sety(enemy.ycor() - 40)
    
    # Mermi hareketi
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + 20)
    
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"
    
    # Vurma Kontrolü
    distance = math.sqrt(math.pow(bullet.xcor()-enemy.xcor(),2) + math.pow(bullet.ycor()-enemy.ycor(),2))
    if distance < 20:
        enemy.goto(-200, 250)
        bullet.hideturtle()
        bullet_state = "ready"
        print("Düşman Vuruldu! 🔥")