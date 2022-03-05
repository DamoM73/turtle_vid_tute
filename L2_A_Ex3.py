import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

###############################
## Draw a Hexagon in 3 lines ##
###############################

for index in range(0, 6):
    my_ttl.forward(100)
    my_ttl.left(60)
