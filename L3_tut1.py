import turtle

screen = 500
sides = 6
length = 100
degrees = 360 / sides

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(degrees)