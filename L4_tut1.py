import turtle

screen = 500
sides = int(input("Number of sides> "))
length = int(input("Length of sides> "))

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)