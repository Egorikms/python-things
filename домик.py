import turtle 

t = turtle.Turtle()

t.penup()
t.goto(-50, 50)
t.pendown()

for i in range(4):
    t.forward(100)
    t.right(90)

t.left(45)
t.backward(15)
t.forward(85)
t.right(90)
t.forward(85)
t.backward(15)

t.penup()
t.goto(-20, 20)
t.pendown()
t.left(45)

for i in range(4):
    t.forward(40)
    t.right(90)

t.forward(20)
t.right(90)
t.forward(40)
t.left(90)

t.penup()
t.goto(-20, 0)
t.pendown()
t.forward(40)

t.penup()
t.goto(30, -50)
t.pendown()
t.left(90)

t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)

t.right(180)



turtle.exitonclick()
