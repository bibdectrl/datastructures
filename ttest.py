import turtle

myturt = turtle.Turtle()
mywin = turtle.Screen()

def draw(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(45)
        myTurtle.left(10)
        myTurtle.forward(lineLen)
        draw(myTurtle, lineLen - 1)

draw(myturt, 100)
mywin.exitonclick()        
