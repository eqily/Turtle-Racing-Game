from turtle import *
from random import randint

lines = 16

speed(25)
penup()
goto(-140, 140)

for step in range(lines):
  write(step, align = 'center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(21)

  #racetrack code ends here, everything below is lining up turtles

Red = Turtle()
Red.color('red')
Red.shape('turtle')

Red.penup()
Red.goto(-160, 100)
Red.pendown()

Blue = Turtle()
Blue.color('blue')
Blue.shape('turtle')

Blue.penup()
Blue.goto(-160, 70) #space the starting positions out by 30 pixels down
Blue.pendown()

Yellow = Turtle()
Yellow.color('yellow')
Yellow.shape('turtle')

Yellow.penup()
Yellow.goto(-160, 30)
Yellow.pendown()

Green = Turtle()
Green.color('cyan')
Green.shape('turtle')

Green.penup()
Green.goto(-160, 0)
Green.pendown()

#next week we will begin here, randomly moving the turtles forward

for turn in range(lines *7):
  Red.forward(randint(1,5))
  Blue.forward(randint(1,5))
  Yellow.forward(randint(1,5))
  Green.forward(randint(2,3))