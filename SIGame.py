import turtle
turtle.tracer(0)


# setup the screen and add pictures
screen = turtle.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.bgpic("space.png")
screen.addshape('battleship_2.gif')
screen.addshape('enemy1.gif')
screen.addshape('yellow.gif')
screen.addshape('bullet.gif')


# Points display at top left
turtle.hideturtle()
turtle.color('white')
turtle.penup()
turtle.setpos(-380, 250)
turtle.pendown()
turtle.write("Points:", False, align="left", font=("Arial", 30, ""))

# Variable called points
points = 0;

# Boolean to see if alien is hit (if true, will update points)
isHit = False


# put the battleship on the screen
ship = turtle.Turtle()
ship.shape('battleship_2.gif')
ship.speed(0)
ship.penup()
ship.setpos(0, -250)


# This is for the power up we can do to increase the speed of the battleship so we can shoot more aliens
# Once the boolean is set to true, the battleship will go faster
speedPU = False;


# functions to move the battle ship
def ship_left():
    x = ship.xcor()
    if speedPU:
        x -= 30
    else:
        x -= 7
    if x < -368:
        x = -368
    ship.setx(x)


def ship_right():
    x = ship.xcor()
    if speedPU:
        x += 30
    else:
        x += 7
    if x > 368:
        x = 368
    ship.setx(x)


# make the battleship move by listening to user input
screen.listen()
screen.onkeypress(ship_left, "Left") # "Left" means left arrow
screen.onkeypress(ship_right, "Right") # "Right" means right arrow


# put one enemy on the screen
enemy = turtle.Turtle()
enemy.shape('enemy1.gif')
# Yellow is the special powerup alien
# enemy.shape('yellow.gif')
enemy.penup()
enemy.speed(0)
enemy.setpos(-300, 250)
# Original speed = 0.15
enemyspeed = 0.15


# main loop for the game
var = True
while var:
    # move the enemy
    x = enemy.xcor()
    x += enemyspeed # move the enemy 0.15 pixels
    enemy.setx(x)
    # move the enemy back and down
    if enemy.xcor() > 360:
        y = enemy.ycor()
        y -= 45 # change the position of the enemy down 45 pixels
        enemyspeed *= -1 # so the enemy moves back the other way
        enemy.sety(y) # move the enemy down

    if enemy.xcor() < -368:
        y = enemy.ycor()
        y -= 45
        enemyspeed *= -1 # - and - make a positive
        enemy.sety(y)

    # If you think its too low, change the -200 to something else
    if enemy.ycor() < -200:
        # y = enemy.ycor()
        var = False
        # y = 250
        # enemy.sety(y)

    # Update points if alien is hit
    if isHit:
        points += 1
        isHit = False

    screen.update()


# endSc = turtle.Screen()
# endSc.title("Space Invaders")
# endSc.setup(width=800, height=600)
# endSc.bgcolor('black')


# End Screen with Points
if not var:
    turtle.clearscreen()
    screen.bgcolor('#ed5853')
    # screen.bgpic('end.png')

    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(0, 100)
    turtle.pendown()
    turtle.write("Game Over", False, align="center", font=("Arial", 50, "bold"))
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()
    turtle.write("Nice Try", False, align="center", font=("Arial", 30, "bold"))
    turtle.penup()
    turtle.setpos(-50, -150)
    turtle.pendown()
    turtle.write("Points:", False, align="center", font=("Arial", 30, "bold"))
    turtle.penup()
    turtle.setpos(40, -150)
    turtle.pendown()
    turtle.write(points, False, align="left", font=("Arial", 30, "bold"))
    turtle.penup()


while not var:
    screen.update()

    # endSc.update()