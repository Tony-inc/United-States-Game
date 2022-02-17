from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()

screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle_2 = Turtle()
turtle_2.hideturtle()
turtle_2.penup()

score = 0

data = pandas.read_csv("50_states.csv")
the_list_of_states = data.state.to_list()

guessed_states = []


while score < 50:
    the_user_choice = screen.textinput(f"Your score: {score}/50", "Guess the state").title()

    if the_user_choice == "Exit":
        states_to_learn = [state for state in the_list_of_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States to learn.csv")
        break

    if the_user_choice in the_list_of_states:
        coordinates = data[data.state == the_user_choice]
        x = int(coordinates.x)
        y = int(coordinates.y)
        turtle_2.goto(x, y)
        turtle_2.write(the_user_choice, align="center")
        score += 1
        guessed_states.append(the_user_choice)

screen.exitonclick()