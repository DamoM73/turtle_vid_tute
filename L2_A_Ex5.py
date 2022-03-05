import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

######################################################
## Go Crazy and make something amazing with loops!! ##
######################################################

for i in range(6):
    my_ttl.forward(100)
    for j in range(6):
        my_ttl.forward(25)
        my_ttl.backward(25)
        my_ttl.left(60)
    my_ttl.backward(100)
    my_ttl.left(60)