import turtle
t=turtle.Turtle()
t.fd(300)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(300)

#above square shape can be drawn using for loop
import turtle
t=turtle.Turtle()
for i in range(4):
     t.fd(100)
     t.lt(90)
t.speed(1) #fatest:0, fast:10,normal:6, slow(3),slowest(1)
t.lt(45)
t.bk(90)
t.hideturtle()  #hides turtle at the end we can do at any point
t.fd(20)
t.showturtle()

#fill color inside square

t.begin_fill()
t.fillcolor("green") # if this line is not specified fills black
for i in range(4):
     t.fd(150)
     t.lt(90)
t.end_fill()     
