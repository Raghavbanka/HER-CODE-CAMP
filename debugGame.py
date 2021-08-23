# import random library (to randomize enemy location)
# import turtle library
# import platform to add sound effects to the game
import random
import turtle
import winsound

turtle.tracer(0)


# start = True
# begin = True
#
# # setup the start screen with instructions
# screen = turtle.Screen()
# screen.title("Space Invaders")
# screen.setup(width=800, height=600)
# screen.bgcolor("white")
# screen.bgpic("neon.png")
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup()
# pen.setpos(0, 170)
# pen.pendown()
# pen.write("SPACE INVADERS", False, align="center", font=("Times New Roman", 60, "bold"))
# pen.penup()
# pen.setpos(0, 110)
# pen.pendown()
# pen.write("Kill as many aliens as you can before they reach you!", False, align="center", font=("Times New Roman", 20, "italic"))
# pen.penup()
# pen.setpos(300, 30)
# pen.pendown()
# pen.write("BONUS RULES:", False, align="right", font=("Courier", 20, "bold"))
# pen.penup()
# pen.setpos(300, 0)
# pen.pendown()
# pen.write("- Once you gain 8 points, the aliens' speed increases.", False, align="right", font=("Arial", 15, ""))
# pen.penup()
# pen.setpos(300, -20)
# pen.pendown()
# pen.write("- Shoot a yellow alien to gain a power up!", False, align="right", font=("Arial", 15, ""))
# pen.penup()
# pen.setpos(-300, -100)
# pen.pendown()
# pen.write("Keyboard controls:", False, align="left", font=("Courier", 20, "bold"))
# pen.penup()
# pen.setpos(-300, -130)
# pen.pendown()
# pen.write("→         move battleship right", False, align="left", font=("Arial", 15, ""))
# pen.penup()
# pen.setpos(-300, -170)
# pen.pendown()
# pen.write("←         move battleship left", False, align="left", font=("Arial", 15, ""))
# pen.penup()
# pen.setpos(-300, -200)
# pen.pendown()
# pen.write("space     fire a bullet", False, align="left", font=("Arial", 15, ""))
# pen.penup()
# pen.setpos(0, -270)
# pen.pendown()
# pen.write("Press the Up arrow key to start!", False, align="center", font=("Arial", 30, ""))
#
#
# def starting():
#     global begin
#     begin = False
#     screen.clearscreen()
#
#
# screen.listen()
#
# screen.onkeypress(starting, 'Up')
#
#
# while start and begin:
#     screen.update()




# setup the screen and add pictures
# if not begin:
screen = turtle.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.bgpic("neon.png")
screen.addshape('battleship_2.gif')
screen.addshape('enemy1.gif')
screen.addshape('bullet.gif')
screen.addshape('yellow.gif')

# put the battleship on the screen
ship = turtle.Turtle()
ship.shape('battleship_2.gif')
ship.speed(0)
ship.penup()
ship.setpos(0, -263)
# the speed of the battle ship in a variable
shipspeed = 25


# functions to move the battle ship
def ship_left():
    x = ship.xcor()
    x -= shipspeed
    if x < -364:
        x = -364
    ship.setx(x)


def ship_right():
    x = ship.xcor()
    x += shipspeed
    if x > 360:
        x = 360
    ship.setx(x)


## put one enemy on the screen
## enemy = turtle.Turtle()
## enemy.shape('enemy.gif')
## enemy.penup()
## enemy.speed(0)
## enemy.setpos(-300, 250)
# the speed of the enemy in a variable
enemyspeed = 0.15
# put 8 enemies on the screen
num_enemies = 8
enemies = []  # create a list to store the enemies
for v in range(num_enemies):  # create a for loop for the number of enemies
    enemies.append(turtle.Turtle())  # each time, add an enemy to the list enemies
for enemy in enemies:
    enemy.shape('enemy1.gif')
    enemy.penup()
    enemy.speed(0)
    # randomize the enemy location
    enemy.setpos(random.randint(-300, 300), random.randint(170, 200))

# create the bullet
bullet = turtle.Turtle()
bullet.shape('bullet.gif')
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
# the speed of the bullet in a variable (I made this faster just for testing)
bulletspeed = 5
# give the bullet a condition (ready - shooting)
bulletcondition = "ready"


# function to fire the bullet
def fire_bullet():
    global bulletcondition  # global means variable is changable even within func.
    if bulletcondition == "ready":  # only fire a bullet when no bullet is fired
        play_sounds("firing_sound.wav")  # play a firing sound when a bullet is fired
        x = ship.xcor()
        y = ship.ycor() + 15
        bullet.setpos(x, y)
        bullet.showturtle()
        bulletcondition = "shooting"


# create a score counter at top left
counter = turtle.Turtle()
counter.speed(0)
counter.hideturtle()
counter.color('white')
counter.penup()
counter.setpos(-380, 270)
counter.pendown()
counter.write("Points: ", False, align="left", font=("Arial", 15, "bold"))  # print Points: on screen
# the player's score in a variable
points = 0
# print the score on the screen
counter.penup()
counter.setpos(-310, 270)
counter.pendown()
counter.write(points, False, align="left", font=("Arial", 15, "bold"))
counter.penup()


# function that checks collision (bullet hit alien)
def collision(obj1, obj2):  # objs being alien and bullet
    distanceX = obj1.xcor() - obj2.xcor()  # get the distance between the objects
    distanceY = obj1.ycor() - obj2.ycor()  # get the distance between the objects
    if abs(distanceX) < 30 and abs(distanceY) < 30:
        return True
    else:
        return False


# function to play sound effects in the game
def play_sounds(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


# make the battleship move by listening to user input
screen.listen()
screen.onkeypress(ship_left, "Left")  # "Left" means left arrow
screen.onkeypress(ship_right, "Right")  # "Right" means right arrow
screen.onkeypress(fire_bullet, "space")  # "space" means space key

# main loop for the game
var = True
var2 = False

while var and not var2:
    # Special Rule :D
    if points % 8 == 0:
        enemyspeed*1.3

    # make all 8 enemies move
    for enemy in enemies:
        # move the enemy across
        x = enemy.xcor()
        x += enemyspeed  # move the enemy 0.15 pixels
        enemy.setx(x)
        # move ALL the enemies down and back the other direction
        if enemy.xcor() > 360:
            for v in enemies:
                y = v.ycor()
                y -= 45  # change the position of the enemy down 45 pixels
                v.sety(y)  # move the enemy down
            enemyspeed *= -1  # so the enemy moves back the other way
        if enemy.xcor() < -368:
            for v in enemies:
                y = v.ycor()
                y -= 45
                v.sety(y)
            enemyspeed *= -1  # - and - make a positive

        # check collision
        if collision(enemy, bullet):
            play_sounds("collision_sound.wav")  # play sound when enemy is shot
            bullet.hideturtle()  # if collision is true, hide bullet and reset enemy
            enemy.setpos(random.randint(-300, 300), random.randint(170, 200))
            bulletcondition = "ready"  # reset bullet condition so it can fire
            bullet.setpos(0, -300)  # move the bullet to bottom to avoid collision
            points += 1  # add one point
            counter.clear()  # clear (Points: *) from the screen
            counter.setpos(-380, 270)  # re-write the points on the screen
            counter.pendown()
            counter.write("Points: ", False, align="left", font=("Arial", 15, "bold"))
            counter.penup()
            counter.setpos(-310, 270)
            counter.pendown()
            counter.write(points, False, align="left", font=("Arial", 15, "bold"))
            counter.penup()

        # check if the enemy is too low (player loses)
        if enemy.ycor() < -200:
            play_sounds("losing_sound.wav")  # play sound if the enemies win
            var = False

    # move the bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
    # change bullet condition to ready when bullet gets goes past the frame
    if bullet.ycor() > 300:
        bulletcondition = "ready"

    screen.update()

# setup the end screen with points
if not var:
    turtle.clearscreen()
    screen.bgcolor('#ed5853')
    pen1 = turtle.Turtle()
    pen1.speed(0)
    pen1.color("white")
    pen1.penup()
    pen1.setpos(0, 100)
    pen1.pendown()
    pen1.write("GAME OVER", False, align="center", font=("Arial", 50, "bold"))
    pen1.penup()
    pen1.setpos(0, 0)
    pen1.pendown()
    pen1.write("Nice Try!", False, align="center", font=("Arial", 30, "bold"))
    pen1.penup()
    pen1.setpos(-20, -150)
    pen1.pendown()
    pen1.write("Points:", False, align="center", font=("Arial", 30, "bold"))
    pen1.penup()
    pen1.setpos(55, -150)
    pen1.pendown()
    pen1.write(points, False, align="left", font=("Arial", 30, "bold"))
    pen1.hideturtle()

while not var:
    screen.update()