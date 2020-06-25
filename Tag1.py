# setup


# imports modules
import turtle
from playsound import playsound
import time

# window
wn = turtle.Screen()
wn.title("Tag")
wn.setup(width = 800, height = 600)
wn.bgcolor("black")
wn.tracer(0)

# player 1
player_1 = turtle.Turtle()
player_1.shape("turtle")
player_1.color("white")
player_1.speed(0)
player_1.penup()       
player_1.goto(-350,0)

# player 2
player_2 = turtle.Turtle()
player_2.shape("circle")
player_2.speed(0)
player_2.penup()
player_2.color("white")
player_2.goto(350,0)


# commands


# player 1's up command
def up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)
        
#player 1's down command
def down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)

# player 1's left command   
def left():
    x = player_1.xcor()
    x -= 20
    player_1.setx(x)
    
# player 1's right command    
def right():
    x = player_1.xcor()
    x += 20
    player_1.setx(x)

# player 2's up command   
def up1():
    y1 = player_2.ycor()
    y1 += 20
    player_2.sety(y1)

# player 2 's down command    
def down1():
    y1 = player_2.ycor()
    y1 -= 20
    player_2.sety(y1)

# player 2's left command    
def left1():
    x1 = player_2.xcor()
    x1 -= 20
    player_2.setx(x1)

# player 2's right command   
def right1():
    x1 = player_2.xcor()
    x1 += 20
    player_2.setx(x1)

# shows x and y for both players    
def help_():
    print("Player 1", player_1.xcor(),",",player_1.ycor(),
          "\nPlayer 2",player_2.xcor(),",", player_2.ycor())

    
#class
class tag():
    
    # main function
    def __init__(self):

   

        # listens for events
        wn.listen()
        wn.onkeypress(up,"w")
        wn.onkeypress(down, "s")
        wn.onkeypress(left, "a")
        wn.onkeypress(right, "d")
        wn.onkeypress(up1,"Up")
        wn.onkeypress(down1, "Down")
        wn.onkeypress(left1, "Left")
        wn.onkeypress(right1, "Right")
        wn.onkeypress(help_,"h")
       
        #game loop   
        while True:
            
            wn.update()
            if player_1.xcor() == player_2.xcor() and player_1.ycor() == player_2.ycor():
                playsound("Wbounce.wav")
                player_2.color("black")
                print("Game Over")
                
            else:
                pass
            
       
#starts the game
c = tag()
