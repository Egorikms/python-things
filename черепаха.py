import turtle



square = turtle.Turtle()


square.color("blue", "blue")
square.begin_fill()
square.forward(200)
square.backward(400)
square.left(90)
square.forward(140)
square.right(90)
square.forward(400)
square.right(90)
square.forward(140)
square.end_fill()

square.color("yellow", "yellow")
square.begin_fill()
square.forward(140)
square.right(90)
square.forward(400)
square.right(90)
square.forward(140)
square.right(90)
square.forward(400)
square.right(90)
square.forward(140)
square.end_fill()

turtle.exitonclick()