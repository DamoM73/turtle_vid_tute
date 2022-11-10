import turtle

window = turtle.Screen()
window.setup(500, 500)

ralph = turtle.Turtle()

## Write your code below this line ##

num_of_side = 100

for side in range(num_of_side):
    ralph.forward(side)
    ralph.left(360/num_of_side)
