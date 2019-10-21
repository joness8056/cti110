# Turtle Graphics Repeating Squares
# 10-17-2019
# CTI-110 P4T1a - Shapes 
# Steve Jones


# Repeating Squares
# Draw 100 Squares

import turtle

OFFSET = 3
STARTING_RADIUS = 10

radius = STARTING_RADIUS

for times in range(100):
    
    turtle.forward(radius)
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(90)

    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    radius = radius + OFFSET
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
