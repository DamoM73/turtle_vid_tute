import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

# draw boarder
my_ttl.penup()
my_ttl.goto(-240,-240)
my_ttl.pendown()
for i in range(4):
    my_ttl.forward(470)
    my_ttl.left(90)
my_ttl.penup()
my_ttl.goto(0,0)
my_ttl.pendown()

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)