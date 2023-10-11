import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800, height=400)
user_choice = screen.textinput(title="Make ur bet!", prompt="Which turtle will win? Make a guess")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtles = []
x = -110
y = 0
race_on = False

for objects in range(6):
    new_turtule = Turtle("turtle")
    new_turtule.color(colors[y])
    y += 1
    new_turtule.penup()
    x += 20
    new_turtule.goto(x=-390, y= x)
    new_turtule.speed("fastest")
    all_turtles.append(new_turtule)

if user_choice:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            race_on = False
            winning_turtle = turtle.pencolor()
            if user_choice == winning_turtle:
                print(f"U guessed Right!! {winning_turtle} WON")
            else:
                print(f"U guessed wrong!! {winning_turtle} WON")
        moving_distance = random.randint(0, 10)
        turtle.forward(moving_distance)







screen.exitonclick()
