import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
guessed_states = []



# print(answer_state)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


# if answer state is one of the states in the 50_states_.csv
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state""s name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
    # if they got it right :
       #create a turtle to write he name of the state at the state's x and y coord
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# keeps our screen running
# turtle.mainloop()
screen.exitonclick()
