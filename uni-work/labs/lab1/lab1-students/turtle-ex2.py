import turtle
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')

t.penup()
t.goto(-300,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)

# your code should go right after this line
#*waves
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)
t.setheading(-45)
t.circle(50,90)

#*sun
t.penup()
t.goto(-100,200)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,-50)

#exit on click
s.exitonclick()