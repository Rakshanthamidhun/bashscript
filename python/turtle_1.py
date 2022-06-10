import turtle
raksh=turtle.Turtle()        #create turtle obj from turtle class
print(raksh.shape())
print(raksh.shape("turtle")) #shape can be specified
print(help(turtle.shape))
print(raksh.color()) #output: ('black', 'black') --> line and turtle
print(raksh.forward(100))  #turtle moves forward with line
print(raksh.color("red"))  #turtle colour turns red
print(raksh.forward(100))  #line also turns red
print(raksh.color("blue","green")) #line:blue, turtle:green
print(raksh.backward(100)) #backward movement of turtle
#we can't set rgb color directly raksh.color(120,40,50) throws error
#set color mode and try rbg color
print(turtle.colormode(255))
print(raksh.color(12,40,50))

wn=turtle.Screen() #create obj for screen
print(wn.bgcolor("purple"))  #background color

print(wn.title("rakshantha"))  #title of graphics
#background image should be in gif format
#print(wn.bgpic("python.gif")) #shows this pic in background
print(wn.bgpic()) #output: nopic, if present displays pic name

print(raksh.setheading(90))
print(raksh.setheading(180))
print(raksh.setheading(270))
print(raksh.setheading(0))
print(raksh.left(45))
print(raksh.fd(250))
print(raksh.right(80))
print(raksh.bk(30))



