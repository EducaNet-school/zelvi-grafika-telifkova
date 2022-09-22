import turtle

def draw_square(t, sz):
    for i in range(4):
        t.left(90)
        t.forward(sz)

def concentric_squares(t, sz, n):
    for i in range(n):
        draw_square(t, sz)
        t.penup()
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        sz+=40

johnny=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("white")
johnny.color("black")
johnny.pensize("3")

concentric_squares(johnny, 20, 6)
wn.exitonclick()
