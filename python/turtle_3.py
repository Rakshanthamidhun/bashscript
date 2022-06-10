import turtle
#circle(radius,extent: says circle or sem-circle,steps: adds polyogan based on sides)
#extent :+angle (clockwise), -angle (anti-clockwise)

t=turtle.Turtle()
t.circle(30)
t.circle(-40)
t.reset()
t.circle(100,180)
t.reset()
t.circle(100,steps=3)
t.circle(150,steps=6)

#till now we saw drawing from home position
t.circle(100)
t.undo()
t.rt(90)
t.fd(100)
t.lt(90)
t.circle(100) #we see line inside circle when turtle moves
#to avoid the line we have
t.reset()
t.goto(0,-150)
t.circle(20)

t.up()
t.goto(0,100)
t.circle(30) #we can't see circle since turtle is up
t.down()
t.circle(100)
t.reset()
t.up() #penup or pu or up
t.goto(100,100)
t.circle(100) #we can't see circle since turtle is up
t.down() #pendown or pd or down
t.circle(100)
#a=turtle.Pen() is same like a=turtle.Turtle



