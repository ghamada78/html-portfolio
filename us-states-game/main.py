import turtle
from turtle import Turtle, Screen
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
gabe = Turtle()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
print (state_list)

correct_guesses = []
score = 0
game_on=True
while game_on:
    answer_state = screen.textinput(title=f"Guess the State-{score}/50", prompt="What's another state's name?")
    state_guess = answer_state.title()
    print(state_guess)
    if state_guess == "Quit":
        game_on = False
        print (state_list)
        break
    if state_guess in state_list:
        print("found!")
        answer_row = data[data.state == state_guess]
        gabe.penup()
        gabe.hideturtle()
        gabe.goto(int(answer_row.x.iloc[0]), int(answer_row.y.iloc[0]))
        gabe.write(state_guess, align="center")
        correct_guesses.append(state_guess)
        state_list.remove(state_guess)
        score += 1
    else:
        print("not found!")
        continue
    print (correct_guesses, score)
    if score == 50:
        print ("You win!")
        game_on = False
screen.exitonclick()