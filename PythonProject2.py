#Name: Joseph White
#Teacher: Tom Bloomfield
#Class: CS 115
#Program: Python Program Project 2

#importing turtle
import turtle
turtle.setup(600, 600)
turtle.penup()

#assigning shape with input and casing input to be read as int
#placing turtle curser in a better starting position so that the shape won't go off screen
#also validating so that the only option to pick is 1, 2, or 3
shape = int(input("Please pick which shape to draw:\n1. Circle \n2. Square \n3. Right Triangle \n"))


#assigning pen with input and casing input to be read as int
pen = input("Please pick a pen color: ")
turtle.pencolor(pen)

#assigning background with input and casing input to be read as int
background = input("Please pick a background color: ")
turtle.bgcolor(background)

#assigning fill with input and casing input to be read as int
fill = input("Please pick a fill color: ")
turtle.fillcolor(fill)

#assigning dimensions for shapes and validating so that the shape can't go off screen
if shape == 1:
    dimension = int(input("Please enter the radius for the circle: "))

elif shape == 2:
    dimension = int(input("Please enter the length of a side: "))

elif shape == 3:
    dimensionLeg1 = int(input("Please enter size of leg one: "))

    dimensionLeg2 = int(input("Please enter size of leg two: "))


#drawing shape based on shape chosen and dimension assigned
turtle.pendown()
if shape == 1:
    turtle.goto(0, -dimension)
    turtle.begin_fill()
    turtle.circle(dimension)
    turtle.end_fill()
elif shape == 2:
    turtle.goto((-dimension // 2), (-dimension // 2))
    turtle.begin_fill()
    turtle.forward(dimension)
    turtle.left(90)
    turtle.forward(dimension)
    turtle.left(90)
    turtle.forward(dimension)
    turtle.left(90)
    turtle.forward(dimension)
    turtle.end_fill()
elif shape == 3:
    if dimensionLeg1 > dimensionLeg2:
        turtle.goto((-dimensionLeg1 // 2), (-dimensionLeg2 // 2))
    else:
        turtle.goto((-dimensionLeg2 // 2), (-dimensionLeg1 // 2))
    turtle.begin_fill()
    x = turtle.pos()
    if dimensionLeg1 > dimensionLeg2:
        turtle.forward(dimensionLeg1)
    else:
        turtle.forward(dimensionLeg2)
    y = turtle.pos()
    turtle.goto(x)
    turtle.left(90)
    if dimensionLeg1 < dimensionLeg2:
        turtle.forward(dimensionLeg1)
    else:
        turtle.forward(dimensionLeg2)
    turtle.goto(y)
    turtle.end_fill()


