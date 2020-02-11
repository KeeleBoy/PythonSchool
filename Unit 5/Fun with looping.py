#Fun with looping
#Basic loops

import turtle
t=turtle.Turtle()
t.pensize(2)
t.color('blue')

#For loop
#for x in range(1,250):
#    print(x)
#    t.fd(x+20)
#    t.rt(92)

x=1
while x < 25:
#    print (x)
    t.fd(x+20)
    t.rt(92)
    x += 1
