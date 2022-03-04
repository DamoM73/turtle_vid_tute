import turtle

def draw_shape(sides,length):
    # draw a shape with given sides and given length
    for i in range(sides):
        my_ttl.forward(length)
        my_ttl.left(360/sides)

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

draw_shape(6,100)
my_ttl.penup

draw_shape(4,100)
draw_shape(3,100)

    
