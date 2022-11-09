import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()


##############################
## Draw a square in 3 lines ##
##############################


for sides in range(200):
    my_ttl.forward(sides)
    my_ttl.right(20)