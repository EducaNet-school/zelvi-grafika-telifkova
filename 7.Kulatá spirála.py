import turtle

a = turtle.Turtle()
for i in range(250):
    a.forward(2+i/4)
    a.left(30-i/12)

turtle.done()
