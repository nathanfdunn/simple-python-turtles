from assets import *

sam = Turtle()
jerome = Turtle()
tammy = Turtle()
seth = Turtle()

def teleportWithoutTrail(turtle, x, y):
	raiseTail(turtle)
	teleport(turtle, x, y)
	lowerTail(turtle)

teleportWithoutTrail(sam, 100, -150)
teleportWithoutTrail(jerome, -100,-100)
teleportWithoutTrail(tammy, 100, 100)
teleportWithoutTrail(seth, -100, 100)

setRgbColor(sam, 153, 56, 0)
for i in oneTo(5):
	move(sam, 100)
	turn(sam, 144)

setRgbColor(jerome, 128, 255, 0)
for i in oneTo(15):
	move(jerome, i*10)
	turnRight(jerome)

setRgbColor(tammy, 128, 0, 255)
for i in oneTo(10):
	drawCircle(tammy, i*5)
	turn(tammy, 30)

setRgbColor(seth, 0, 0, 255)
for i in oneTo(15):
	drawArc(seth, i*5, 180)
