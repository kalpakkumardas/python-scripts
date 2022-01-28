import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States")
image = "India_map.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("data.csv")
x = states_data["X "].to_list()
y = states_data["Y"].to_list()
states_name = states_data["State"].to_list()
turtle.penup()
turtle.speed(0)
turtle.tracer(0)
gg = True
score = 0
correct_states = []

while gg and score <= len(states_data):
    answer_state = screen.textinput(title=f"{score}/37 Guess the State or Union Territory",
                                    prompt="What's the state's name ?(if you want to exit type "
                                           "'exit)").lower()
    for i in range(0, len(states_name)):
        if answer_state == states_name[i].lower() and answer_state not in correct_states:
            score += 1
            correct_states.append(answer_state)
            x_go = int(x[i])
            y_go = int(y[i])
            turtle.goto(x_go, y_go)
            turtle.write(states_name[i], move=False, align='center', font=('Arial', 8, 'bold'))
        elif answer_state == 'exit':
            gg = False
        else:
            pass

        turtle.goto(0, 0)
turtle.mainloop()

print(f"Yor final score was {score} out of 37 states and union territories")
print("The correct states you have guessed were :")
for j in correct_states:
    print(j)


