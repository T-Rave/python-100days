import random

NUMBER_TO_GUESS = random.randint(1,100)

def difficulty():
    diff_choice = input('Choose a difficulty. Type "easy" or "hard": ')
    if diff_choice == 'easy':
        return 10
    elif diff_choice == 'hard':
        return 5
    else:
        print("You didn't do something right")
        return

def check_guess(guess):
    if guess == NUMBER_TO_GUESS:
        return "Great job, you guessed right!"
    elif guess < NUMBER_TO_GUESS:
        return "Too low"
    elif guess > NUMBER_TO_GUESS:
        return "Too high"

def end_game(guess):
    if guess != NUMBER_TO_GUESS and chances_left == 1:
        print("You lose")
        return chances_left * 0
    elif guess != NUMBER_TO_GUESS:
        print(f"{chances_left -1} chances left. Guess again")
        return chances_left - 1
    elif guess == NUMBER_TO_GUESS:
        print('You win!')
        return chances_left * 0

chances_left = difficulty()
while chances_left > 0:
    guess = int(input('What is your guess?\n'))
    print(check_guess(guess))
    chances_left = end_game(guess)
    

