"""import turtle
t=turtle.Turtle()
t.up()

t.goto(0,-50)
t.down()
t.begin_fill()
t.fillcolor("green")
t.circle(50)
t.end_fill()
t.up()
t.home()

t.goto(200,200)
t.down()
t.begin_fill()
t.fillcolor("orange")
t.circle(50)
t.end_fill()
t.up()
t.home()

t.goto(-200,200)
t.down()
t.begin_fill()
t.fillcolor("blue")
t.circle(50)
t.end_fill()
t.up()
t.home()

t.goto(-200,-200) 
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(50) #-50 to fix space(anti-clock)
t.end_fill()
t.up()
t.home()

t.goto(200,-200)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.circle(50)  #-50 to fix space(anti-clock)
t.end_fill()
t.up()
t.home()"""

#above can be written in this
def draw_circle(x,y,color,rad):
     t.goto(x,y) 
     t.down()
     t.begin_fill()
     t.fillcolor(color)
     t.circle(rad) 
     t.end_fill()
     t.up()
     t.home()

import turtle
t=turtle.Turtle()
t.up()
draw_circle(0,-50,"green",50)
draw_circle(200,200,"orange",50)
draw_circle(-200,200,"blue",50)
draw_circle(-200,-200,"red",-50)
draw_circle(200,-200,"yellow",-50)

























