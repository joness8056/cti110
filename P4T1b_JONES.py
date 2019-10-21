# rite a program that displays your first and last initials.
# 10-17-2019
# CTI-110 P4Tb - Initials
# Steve Jones 

# Turtle Graphics to display my
# First and last initals
# use Penup and Pendown

import turtle

turtle.showturtle()

START_X = 100
START_Y = 0

turtle.forward(-100)
turtle.left(-90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(-50)
turtle.left(-90)
turtle.forward(-100)
turtle.left(-90)
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(-50)
turtle.left(-90)
turtle.forward(-50)
turtle.left(-90)

