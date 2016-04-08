import turtle as t
import time

# Basics
def Turtle():
	time.sleep(0.4)
	out = t.Turtle()
	out.hideturtle()
	out.shape('turtle')
	out.speed(0)
	out.left(90)
	out.showturtle()
	out.speed(10)
	return out

def move(turtle, distance):
	turtle.forward(distance)

def turnRight(turtle):
	turtle.right(90)
	
def turnLeft(turtle):
	turtle.left(90)

def setColor(turtle, color):
	turtle.color(color)

def oneTo(n):
	return range(1, n+1)

# Advanced
def turn(turtle, degrees):
	turtle.left(degrees)

def drawCircle(turtle, radius):
	turtle.circle(radius)

def drawArc(turtle, radius, degrees):
	turtle.circle(radius, degrees)

def raiseTail(turtle):
	turtle.penup()

def lowerTail(turtle):
	turtle.pendown()

def teleport(turtle, x, y):
	turtle.goto(x,y)
	
def setSpeed(turtle, speed):
	turtle.speed(speed)

def setRgbColor(turtle, r, g, b):
	turtle.color(r, g, b)

def reset(turtle):
	isdown = turtle.isdown()
	turtle.penup()
	turtle.goto(0,0)
	turtle.setheading(90)
	turtle.clear()
	turtle.color('black')
	if isdown:
		turtle.pendown()

def delete(turtle):
	turtle.hideturtle()
	turtle.pendown()

# Random
def doStuff(x):
	print 'Doing stuff:'
	for i in range(3):
		print 'do'
	print 'Did stuff with:', x
