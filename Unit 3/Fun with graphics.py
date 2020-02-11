#Fun with graphics
import turtle

t = turtle.Turtle()
t.pensize(5)


#Draw line
t.pencolor('red')
t.fd(250)
t.pencolor('blue')
t.right(90)
t.fd(250)
t.pencolor('green')
t.right(90)
t.fd(250)
t.right(90)
t.pencolor('orange')
t.fd(250)

t.pu()

t.pencolor('red')
t.setpos (25,5)

t.pd()

t.fd(250)
t.pencolor('blue')
t.right(90)
t.fd(250)
t.pencolor('green')
t.right(90)
t.fd(250)
t.right(90)
t.pencolor('orange')
t.fd(250)

t.speed('slowest')
t.pencolor('blue')
for x in range (1,20):
    t.fd(70)
    t.right(360/12)
    t.circle (25)
    t.dot(25)
