import turtle

t = turtle.Turtle()

t.penup()
t.goto(0, 50)
t.pendown()

t.pensize(5)

t.color("black", "black")
t.begin_fill()
t.forward(400)
t.backward(800)
t.left(90)
t.forward(200)
t.right(90)
t.forward(800)
t.right(90)
t.forward(200)
t.end_fill()

t.color("yellow", "yellow")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(800)
t.right(90)
t.forward(200)
t.right(90)
t.forward(800)
t.right(90)
t.forward(200)
t.end_fill()

t.color("black", "white")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(800)
t.right(90)
t.forward(200)
t.right(90)
t.forward(800)
t.right(90)
t.forward(200)
t.end_fill()

turtle.exitonclick()