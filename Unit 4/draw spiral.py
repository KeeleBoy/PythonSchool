import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize (2000,1500,"blue")
screen.title('demo')

t.pensize(2)
t.speed("normal")
t.pencolor('red')

for x in range(1,200):
    t.fd(x+15)
    t.right(95)
