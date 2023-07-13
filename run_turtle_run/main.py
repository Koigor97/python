from  turtle import Turtle, Screen
import random

who_won = False
colors = ["red", "blue", "gold1", "purple", "green", "SkyBlue1"]
positions = [-250, -150, -50, 50, 150, 250]
x_cor = -360
runners = []

def new_turtles():
    for n in range(0, len(colors)):
        racer = Turtle()
        racer.penup()
        racer.shape("turtle")
        racer.color(colors[n])
        racer.setposition(x=x_cor, y=positions[n])
        runners.append(racer)


# Screen setup configurations
screen = Screen()
screen.title("🐢...Run Turtle Run...🐢")
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle you think is going to win? (Red, Blue, Gold1,"
                                                          " Purple, Green, Sky Blue) Enter the color").lower()
winner = ""

# set up the track
new_turtles()
while not who_won:
    for runner in runners:
        if round(runner.xcor()) < 369:
            runner.fd(random.randint(1, 10))

        else:
            who_won = True
            winner = runner.pencolor()
            break

if user_bet == winner:
    print(f"You won the best. The winner is: {winner.title()}.  Your prize $500")
else:
    print(f"You lost the best. The winner is: {winner.title()}.  You lost $500")



screen.exitonclick()