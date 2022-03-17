import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()

def draw_square(length):
    for i in range(4):
        my_ttl.forward(length)
        my_ttl.right(360 / 4)
        
def draw_triangle(length):
    for i in range(3):
        my_ttl.forward(length)
        my_ttl.left(120)

def draw_rectangle(hor,vert):
    for i in range(2):
        my_ttl.forward(hor)
        my_ttl.left(90)
        my_ttl.forward(vert)
        my_ttl.left(90)

def draw_circle(size):
    my_ttl.circle(size)

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

move_pen(-100,0)
draw_square(200)
draw_triangle(200)
move_pen(-25,-200)
draw_rectangle(50,100)    
move_pen(-80,-100)
draw_square(35)
move_pen(45,-100)
draw_square(35)
move_pen(15,-150)
draw_circle(5)
my_ttl.circle(5)
my_ttl.hideturtle()