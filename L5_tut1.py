import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

# get user input
num_sides = input("How many sides?> ")
if num_sides.isdigit():
    num_sides = int(num_sides)
else:
    print("Invalid input")
    quit()

size = input("How long are the sides?> ")
if size.isdigit():
    size = int(size)
else:
    print("Invalid input")
    quit()

draw_poly(size,num_sides)