import  turtle
import  pandas
import  time
screen = turtle.Screen()
screen.title("USA States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
shtati = list(states.state)
shtatimisses = shtati
process = []
some = 0
length = 0
while length < 50:
    answer = screen.textinput(title=f"{some}/50 Guess the state", prompt="What's the state's name").title()
    if answer in shtati:
        aka = turtle.Turtle()
        aka.hideturtle()
        aka.penup()
        data = states[states.state == answer]
        cords = int(data.x), int(data.y)
        aka.goto(cords)
        aka.write(f"{answer}", font=("JetBrains Mono", 8, "bold"))
        if answer not in process:
            some += 1
        process.append(answer)
        one = [each for each in shtatimisses if each != answer]
        shtatimisses = one
        length += 1
    elif answer == "Exit":
        newd = pandas.DataFrame(one)
        newd.to_csv("miss.csv")
        break
    elif answer not in shtati:
        aka = turtle.Turtle()
        aka.hideturtle()
        aka.goto(0, 0)
        aka.color("red")
        aka.write(f"'{answer}' is an Incorrect!", font=("JetBrains Mono", 24, "bold"), align="center")
        time.sleep(2)
        aka.clear()

