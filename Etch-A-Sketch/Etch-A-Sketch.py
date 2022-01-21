from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_everything():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_everything)
screen.exitonclick()
