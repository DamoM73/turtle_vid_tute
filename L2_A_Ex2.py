import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

################################
## Draw a Triangle in 3 lines ##
################################

for index in range(0, 3):
    my_ttl.forward(150)
    my_ttl.left(120)