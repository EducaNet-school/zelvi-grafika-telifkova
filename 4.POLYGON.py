from turtle import * 
import turtle as turt

tur = turt.Turtle()
 
sides = 10

length = 100  
  
for _ in range(sides):
    turt.forward(length)
    turt.right(360 / sides)
turt.done()