import pandas
import turtle

screen = turtle.Screen()
screen.title('🗺️ U.S. States Game 🗺️')

# load in a new image as a new shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Boolean to keep the game running
game_is_on = True

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
    answer_state = screen.textinput (title=message, prompt='Guess a State')
    guess = answer_state
    print(guess)

    # Check if the state is correct
    if guess in df.values:
        print('Element Exists')
        correct_guesses += 1
        correct_states.append(guess)
        print('elements inside the list: ', correct_states)
        print(correct_guesses)
    else:
        print('lokura')

# get the coordinates in the map
# this can help you create another map from another country if you like
# def get_mouse_click_coor(x,y)
    #print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()
