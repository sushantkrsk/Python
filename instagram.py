from turtle import *
#Turtle” is a Python feature like a drawing board,
# which lets us command a turtle to draw all over it.
bgcolor('#962170')
pencolor('#f3f3f3')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
 forward(250)
 circle(34,90)

penup()
goto(85,30)
pendown()

begin_fill()
circle(80,360)

penup()
goto(110,130)
pendown()
circle(7,360)

done()