import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

#################################################
## Draw a circle (hint - you only need 3 lines ##
#################################################

for index in range(0, 360):
    my_ttl.forward(1)
    my_ttl.left(1)