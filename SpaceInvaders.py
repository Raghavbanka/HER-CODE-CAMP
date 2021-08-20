import turtle


# Screen and pictures
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.addshape('battleship_2.gif')
# screen.bgpic('redBg.png')
screen.bgpic('space.png')


# Battleship
ship = turtle.Turtle()
ship.shape('battleship_2.gif')
# ship.shapesize(2)
ship.speed(0)
ship.penup()
ship.goto(0, -250)
screen.listen()


# This is for the power up we can do to increase the speed of the battleship so we can shoot more aliens
# Once the boolean is set to true, the battleship will go faster
speedPU = False;


# Function to move battleship left
def left():
    x = ship.xcor()
    if speedPU:
        x -= 30
    else:
        x -= 7
    if x < -368:
        x = -368
    ship.setx(x)


# Function to move battleship right
def right():
    x = ship.xcor()
    if speedPU:
        x += 30
    else:
        x += 7
    if x > 368:
        x = 368
    ship.setx(x)


screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')


var = True
while var:
    screen.update()