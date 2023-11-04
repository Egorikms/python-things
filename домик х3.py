import turtle 

t = turtle.Turtle()

t.pensize(10)

t.penup()
t.goto(-100, 100)
t.pendown()

for i in range(4):
    t.forward(200)
    t.right(90)

t.left(45)
t.backward(30)
t.forward(173)
t.right(90)
t.forward(173)
t.backward(30)

t.penup()
t.goto(-40, 40)
t.pendown()
t.left(45)

for i in range(4):
    t.forward(80)
    t.right(90)

t.forward(40)
t.right(90)
t.forward(80)
t.left(90)

t.penup()
t.goto(-40, 0)
t.pendown()
t.forward(80)

t.penup()
t.goto(60, -100)
t.pendown()
t.left(90)

t.forward(80)
t.right(90)
t.forward(40)
t.right(90)
t.forward(80)

t.right(180)



turtle.exitonclick()
