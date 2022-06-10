import turtle
t=turtle.Turtle()
list=["yellow","red","blue","green"]
t.up()
t.goto(200,0)
for i in range(4):
     t.down()
     t.begin_fill()
     t.pensize(10) #thickness
     t.fillcolor(list[i])
     #t.color(list[i]) to change thickeness color instead of black
     t.circle(50)  #increase radius for circle to overlap
     t.end_fill()
     t.up()
     t.bk(100)

t.reset()
list1=["purple","red","orange","blue","green"]
for i in range(40):
     t.color(list1[i%5])
     t.pensize(i/10+1)
     t.fd(i)
     t.lt(59)

