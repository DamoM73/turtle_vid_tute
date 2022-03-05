import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

##############################
## Draw a square in 3 lines ##
##############################

for index in range(0, 4):
    my_ttl.forward(200)
    my_ttl.left(90)