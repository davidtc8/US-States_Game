import pandas
import turtle
import time

screen = turtle.Screen()
screen.setup(width=700, height=550)
screen.title('🗺️ U.S. States Game 🗺️')

# load in a new image as a new shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Boolean to keep the game running
game_is_on = True
style = ('Courier', 10, 'bold')

# Number of guesses correct
correct_guesses = 0

# Record correct guesses in a list
correct_states = []

# read the csv file
df = pandas.read_csv ('50_states.csv')

while game_is_on:
    # check the correct guess
    message = f'Correct States {correct_guesses}/50'

    # check the answer
    answer_state = screen.textinput (title=message, prompt='Guess a State').title()
    guess = answer_state
    print(guess)

    # Check if the state is correct
    if guess in df.values:
        print('Element Exists')
        correct_guesses += 1
        correct_states.append(guess)
        word = turtle.Turtle()
        word.hideturtle()
        word.penup()
        position = df[df.state == guess]
        position_x = int(position.x)
        position_y = int(position.y)
        print(position_x, position_y)
        word.goto(position_x, position_y)
        word.write(guess, font=style, align='center')
        print('elements inside the list: ', correct_states)
        print(correct_guesses)
    else:
        word_2 = turtle.Turtle()
        word_2.hideturtle()
        word_2.color('red')
        word_2.penup()
        word_2.goto(x=250, y=250)
        word_2.write(f'{guess} is not a state', font=style, align='center')
        time.sleep(2)
        word_2.clear()

# get the coordinates in the map
# this can help you create another map from another country if you like
# def get_mouse_click_coor(x,y)
    #print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()
