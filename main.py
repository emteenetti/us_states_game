import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = 'blank_states_img.gif'

screen.addshape(image)

turtle.shape(image)
gameOn = True
raw_data = pandas.read_csv("50_states.csv")
data = raw_data['state']

state_list = data.to_list()
answers = []
with open("highscore_file.txt") as highscore_data:
    highscore = int(highscore_data.read())
print(highscore)

while gameOn:
    score = len(answers)
    state = screen.textinput(title=f"Score = {score}/50 Highest Score = {highscore}",
                             prompt="What's another state's name").title()
    if state == "exit".title():
        gameOn = False
    if state in state_list and state not in answers:
        answers.append(state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        cord = raw_data[raw_data.state == state]
        t.goto(int(cord.x), int(cord.y))
        t.write(state)
        score = len(answers)
        if score > highscore:
            highscore = score
            with open("highscore_file.txt", mode="w") as highscore_data:
                highscore_data.write(f"{highscore}")
        if len(answers) == 50:
            gameOn = False

# t = turtle.Turtle()
# t.hideturtle()
# t.penup()
# cord = raw_data[raw_data.state == state]
# t.goto(int(cord.x), int(cord.y))
# t.write(state)

screen.exitonclick()
