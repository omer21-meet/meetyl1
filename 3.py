import turtle
from turtle import Turtle


#turtle = turtle.Turtle()

SIZE_X = 1200
SIZE_Y = 1000
turtle.setup(SIZE_X, SIZE_Y)

class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		self.r = r
		self.color = color
		self.dx = dx
		self.dx = dy
	def move(self):
		turtle.goto(dx,dy)
		right_side_ball = dx+r/10
		left_side_ball = dx-r/10
		top_side_ball = dy+r/10
		bottom_side_ball = dy-r/10
Ball.move()

turtle.shape("circle")
turtle.penup()
turtle = Ball("r/10","color","dx","dy")
