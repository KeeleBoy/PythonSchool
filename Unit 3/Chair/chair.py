#twochairs
import turtle

t = turtle.Turtle()

#Draw the chairs

t.dot(25)
t.up()
t.fd (200)
t.down()
t.dot(25)

#start in chair
t.up()
t.home()
t.down()
t.fd(179)

#turn around
t.right(180)

#sit
t.bk(1)
