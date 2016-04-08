from assets import *

tammy = Turtle()

def drawSquare(turtle, sideLength):
	turnRight(turtle)
	move(turtle, sideLength)
	turnRight(turtle)
	move(turtle, sideLength)
	turnRight(turtle)
	move(turtle, sideLength)
	turnRight(turtle)
	move(turtle, sideLength)

setColor(tammy, 'blue')

for i in oneTo(4):
	drawSquare(tammy, 10*i)

setColor(tammy, 'red')

for i in oneTo(5):
	drawSquare(tammy, 40 + 10*i)
