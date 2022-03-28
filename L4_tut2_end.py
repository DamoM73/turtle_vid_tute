import turtle

def draw_poly(length, sides, color):
    fred.color("black", color)
    fred.begin_fill()
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
    fred.end_fill()

def get_num(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid number")
        quit()
        
def get_color():
    color = input("Fill colour (red, blue, green)").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Not a valid colour")
        quit()
    

# setup window
screen = 500
window = turtle.Screen()
window.setup(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = get_num("How many sides?> ")

length = get_num("How long are the length?> ")

color = get_color()



draw_poly(length,sides,color)