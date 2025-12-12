import turtle

wn = turtle.Screen()
wn.title("Simple Paint")
wn.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.shapesize(0.5)
pen.color("black")

def dragging(x, y):
    pen.ondrag(None)
    pen.setheading(pen.towards(x, y))
    pen.goto(x, y)
    pen.ondrag(dragging)

def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

wn.listen()
pen.ondrag(dragging)
wn.onkeypress(clear_screen, "c")

print("Mouse ile çiz, 'c' ile temizle.")
wn.mainloop()   