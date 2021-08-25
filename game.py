# import random library (to randomize enemy location)
# import turtle library
# import platform to add sound effects to the game
import random
import turtle
import winsound
turtle.tracer(0)
turtle.hideturtle()


# setup the screen and add pictures
screen = turtle.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.addshape('battleship.gif')
screen.addshape('enemy.gif')
screen.addshape('bullet.gif')
screen.addshape('powerup.gif')
screen.addshape('start.background.gif')
# boolean to make the game start
start = False
# draw the start screen on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('start.background.gif')
# create the button
button = turtle.Turtle()
button.speed(0)
button.hideturtle()
button.color('#8B008B') # the color of the line it draws
button.pencolor('white') # the color of the object
button_x = 80
button_y = -185
button_length = 200
button_width = 100
button.penup()
button.begin_fill()
button.goto(button_x, button_y)
button.goto(button_x, button_y + button_width)
button.goto(button_x + button_length, button_y + button_width)
button.goto(button_x + button_length, button_y)
button.goto(button_x, button_y)
button.end_fill()
button.penup()
button.goto(180, -163)
button.pencolor("white")
button.write("PLAY", False, align="center", font=("Courier", 40, "bold"))

# function that the button executes
def start_game(x, y) -> None:  # -> None means function will not return anything
    if button_x <= x <= (button_x + button_length):
        if button_y <= y <= (button_y+button_width):
            global start
            start = True
            screen.clear()
            screen.bgpic("neon_background.png")

# making the button 'clickable'
screen.onclick(start_game)
# this loop makes the start screen display until the button is clicked
while not start:
    screen.update()

turtle.tracer(0)

# put the battleship on the screen
ship = turtle.Turtle()
ship.shape('battleship.gif')
ship.speed(0)
ship.penup()
ship.setpos(0, -263)
ship.fire_state: False # variable to see if the battleship is firing
# the speed of the battle ship in a variable
shipspeed = 20
# functions to move the battle ship
def ship_left() -> None:
    x = ship.xcor()
    x -= shipspeed
    if x < -364:
        x = -364
    ship.setx(x)

def ship_right() -> None:
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
enemyspeed = 5
# put 8 enemies on the screen
num_enemies = 8
enemies = [] # create a list to store the enemies
for v in range(num_enemies): # create a for loop for the number of enemies
    enemy = turtle.Turtle()
    enemy.direction = random.choice([-1, 1])
    enemy.speed(0)
    enemy.shape('enemy.gif')
    enemy.penup()
    enemy.is_yellow = False # variable for the yellow enemy
    enemy.setpos(random.randint(-300, 300), random.randint(170, 200)) # randomize enemy location
    enemies.append(enemy) # add the enemy to the list


# create the bullet
bullet = turtle.Turtle()
bullet.shape('bullet.gif')
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
# the speed of the bullet in a variable
bullet.bullet_speed = 20
# give the bullet a condition (ready - shooting)
# bulletcondition = "ready"

# function to initialize the enemy
def initialize_enemy() -> turtle.Turtle: # function returns a turtle in form of an enemy
    alien = turtle.Turtle()
    alien.direction = random.choice([-1, 1])
    alien.speed(0)
    if random.randint(0, 10) == 0: # 1 in 10 chance that it is a yellow alien (rare)
        enemy.shape('powerup.gif')
        enemy.is_yellow = True # make this variable true
    else:
        enemy.shape('enemy.gif') # if it is a normal alien, make it false
        enemy.is_yellow = False
    enemy.penup()
    enemy.setpos(random.randint(-300, 300), random.randint(170, 200))
    return enemy

# function to fire the bullet
def fire_bullet() -> None:
    if not ship.fire_state: # only fire a bullet when no bullet is fired (when the ship is not in a fire state)
        play_sounds("firing_sound.wav") # play a firing sound when a bullet is fired
        x = ship.xcor()
        y = ship.ycor() + 15
        bullet.setpos(x, y)
        bullet.showturtle()
        ship.fire_state = not ship.fire_state


# create a score counter at top left
counter = turtle.Turtle()
counter.speed(0)
counter.hideturtle()
counter.color('white')
counter.penup()
counter.setpos(-380, 270)
counter.pendown()
counter.write("Points: ", False, align="left", font=("Arial", 15, "bold")) # print Points: on screen
# the player's score in a variable
points = 0
# print the score on the screen
counter.penup()
counter.setpos(-310, 270)
counter.pendown()
counter.write(points, False, align="left", font=("Arial", 15, "bold"))
counter.penup()


# function that checks collision (bullet hit alien)
def collision(obj1: turtle.Turtle, obj2: turtle.Turtle) -> bool: # objs being alien and bullet(both turtles), and it returns a boolean
    distance = obj1.distance(obj2)
    if distance < 32:
        return True
    else:
        return False


# function to play sound effects in the game
def play_sounds(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


# make the battleship move by listening to user input
screen.listen()
screen.onkeypress(ship_left, "Left")    # "Left" means left arrow
screen.onkeypress(ship_right, "Right")  # "Right" means right arrow
screen.onkeypress(fire_bullet, "space") # "space" means space key


# main loop for the game
var = True
while var and start:
    turtle.hideturtle()

    # make all 8 enemies move
    for enemy in enemies:
        # move the enemy across
        x = enemy.xcor()
        x += enemyspeed * enemy.direction# move the enemy
        enemy.setx(x)
        # move ALL the enemies down and back the other direction
        if enemy.xcor() > 360 or enemy.xcor() < -368:
                y = enemy.ycor()
                y -= 45 # change the position of the enemy down 45 pixels
                enemy.sety(y) # move the enemy down
                enemy.direction *= -1  # so the enemy moves back the other way
        # check if the enemy is too low (player loses)
        if enemy.ycor() < -200:
            play_sounds("lose.wav")  # play sound if the enemies win
            var = False

    for enemy in enemies:
        # check collision
        if collision(enemy, bullet) and ship.fire_state: # make sure the ship is in fire state
            play_sounds("collision_sound.wav") # play sound when enemy is shot
            if enemy.is_yellow: # if it is the yellow enemy, the ships speed increases (powerup)
                shipspeed += 8
            bullet.hideturtle()  # if collision is true, hide bullet and reset enemy
            enemies.remove(enemy) # remove the enemy from the list
            enemies.append(initialize_enemy()) # add an initialized enemy to the list instead
            ship.fire_state = not ship.fire_state  # reset bullet condition so it can fire
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
            # if player reaches multiple of 8 points, the enemy speed increases
            if points % 8 == 0 and points != 0:
                enemyspeed += 0.8


    # move the bullet only if the ship is in fire state
    if ship.fire_state:
        y = bullet.ycor()
        y += bullet.bullet_speed
        bullet.sety(y)
    # change the ship's fire state to false when bullet gets goes past the frame
    if bullet.ycor() > 300:
        ship.fire_state = False
        bullet.hideturtle()


    screen.update()

# setup the end screen with points
if not var:
    turtle.clearscreen()
    screen.bgpic("end.background.png")
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

count = 200000
while not var:
    screen.update()
    count -= 1
    if count == 0:
        screen.bye()
