import turtle

#################################################
## Change the variable values to draw a circle ##
#################################################

screen = 500
sides = 1
length = 1

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)