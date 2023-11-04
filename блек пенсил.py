import turtle

t = turtle.Turtle()

t.pensize(50)

t.penup()
t.goto(0, -300)
t.pendown()

t.right(90)
t.circle(100)
t.right(180)
t.circle(100)

t.penup()
t.goto(80, -203)
t.pendown()

t.forward(260)
t.backward(45)
t.left(90)
t.forward(160)

t.backward(160)
t.right(90)
t.forward(45)

t.circle(80, 180)

t.forward(260)

t.penup()
t.goto(0, 137)
t.pendown()

t.forward(75)

t.penup()
t.goto(-500, -500)
t.pendown()





turtle.exitonclick()