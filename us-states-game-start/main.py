import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S State Game')
image = '././us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(title="Guess the State", prompt="Whats another states name")


print(answer_state)

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state)