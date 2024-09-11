import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line
#!important methods
#*t.circle(radius)
#*t.penup()
#*t.goto(x, y)
#*t.pendown()

#*circles
#innermost circle
t.circle(10)
t.penup()
t.goto(0, -20)
t.pendown()

#next one
t.circle(30)
t.penup()
t.goto(0, -40)
t.pendown()

#third circle
t.circle(50)
t.penup()
t.goto(0, -60)
t.pendown()

#last circle
t.circle(70)
t.penup()

#*lines
#line1
t.goto(0, 150)
t.pendown()
t.right(90)
t.forward(300)
t.penup()

#line2
t.goto(-150, 10)
t.pendown()
t.left(90)
t.forward(300)
t.penup()

#line3
t.goto(100, 110)
t.pendown()
t.right(135)
t.forward(300)
t.penup()

#line4
t.goto(-100, 110)
t.pendown()
t.left(90)
t.forward(300)
t.penup()

#exit on click
s.exitonclick()