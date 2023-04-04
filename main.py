import turtle
import pandas

FONT = ("Arial", 11, "normal")
ALIGN = "center"

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
us_states = pandas.read_csv("50_states.csv")
state_list = us_states.state.to_list()

guesses = []

while len(guesses) < 50 :
    answer = screen.textinput(title=f"{len(guesses)}/50 States Correct ", prompt="What's another state's name?").title()

    if answer == "Exit":
        not_guessed = [state for state in state_list if state not in guesses]
        data = pandas.DataFrame(not_guessed)
        data.to_csv('state_to_learn.csv')
        break

    if answer in state_list and answer not in guesses:
        guesses.append(answer)
        guessed_state = us_states[us_states.state == answer]
        new_t = turtle.Turtle()
        new_t.hideturtle()
        new_t.penup()
        new_t.speed("fastest")
        new_t.goto(int(guessed_state.x), int(guessed_state.y))
        new_t.write(answer, FONT, ALIGN)
    else:
        pass





