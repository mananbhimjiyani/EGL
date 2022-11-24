import turtle
from turtle import Screen
import math


def lineInFrontOfVP():
    distanceAbove = int(input("Enter the distance above the reference line:- "))
    distanceBelow = int(input("Enter the distance below the reference line:- "))

    turtle.left(90)
    turtle.forward(distanceAbove * 10)
    turtle.right(angle)
    turtle.forward(TL * 10)
    turtle.back(TL * 10)
    turtle.left(angle)
    turtle.back(distanceBelow * 10 + distanceAbove * 10)
    turtle.right(90)
    turtle.forward(FV * 10)


def lineInclinedToVP():
    distanceAbove = int(input("Enter the distance above the reference line:- "))
    distanceBelow = int(input("Enter the distance below the reference line:- "))
    turtle.right(90)
    turtle.forward(distanceBelow * 10)
    turtle.left(angle)
    turtle.forward(TL * 10)
    turtle.back(TL * 10)
    turtle.right(angle)
    turtle.back(distanceAbove * 10 + distanceBelow * 10)
    turtle.left(90)
    turtle.forward(FV * 10)


screen = Screen()
turtle.screensize(10000, 10000)
turtle.title("EGL PROJECT")
turtle.penup()
turtle.goto(-500, 0)
turtle.pendown()
turtle.forward(1000)
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
x = int(input("Please enter if the 1. line is in front of VP or 2. inclined to VP:- "))
angle = (input("Please enter the angle of inclination (If unknown enter unk):- "))
if angle == "unk":
    TL = int(input("Please enter how long (TL) the line is:- "))
    FV = int(input("Pleas enter the length (FV) of line is:- "))
    if TL < FV:
        print("TL cant be smaller then FV")
        exit()
    angle = math.degrees(math.acos(FV / TL))
    print(angle)
elif angle != "unk":
    angle = int(angle)
    d = int(input("Please enter if 1. TL is unknown or 2.FV is unknown:- "))
    if d == 1:
        angle = math.radians(angle)
        FV = int(input("Pleas enter the length(FV) of line is:- "))
        TL = float(FV / math.cos(angle))
        print(TL)
        angle = math.degrees(angle)
    elif d == 2:
        angle = math.radians(angle)
        TL = int(input("Please enter how long (TL) the line is:- "))
        FV = float(math.cos(angle) * TL)
        print(FV)
        angle = math.degrees(angle)
if x == 1:
    lineInFrontOfVP()

if x == 2:
    lineInclinedToVP()

turtle.exitonclick()
