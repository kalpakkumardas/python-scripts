from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -100
all_turtles = []
new_turtle.ht()
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations!! You have won. The {winning_color} turtle won..")
            else:
                print(f"Ooops!! You have lost. The {winning_color} turtle won..")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
