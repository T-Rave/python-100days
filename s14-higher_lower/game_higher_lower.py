import art_higher_lower as art
import data_higher_lower as data
import random

def generate_choice():
    return random.choice(data.data)

def compare_choices(a,b,choice):
    if choice == 'A' or choice == 'a' and a['follower_count'] > b['follower_count']:
        return ['win',a]
    elif choice == 'A' or choice == 'a' and a['follower_count'] < b['follower_count']:
        return ['lose']
    elif choice == 'B' or choice == 'b' and a['follower_count'] > b['follower_count']:
        return 'lose'
    elif choice == 'B' or choice == 'b' and a['follower_count'] < b['follower_count']:
        return ['win',b]

def game():
    print(art.logo)
    print("Goal of the game is to get as many points by choosing the option a higher follower count\n")
    option1 = generate_choice()
    option2 = generate_choice()
    is_correct = True
    correct_count = 0
    while is_correct:
        if option1 == option2:
            option2 = generate_choice()
        else:
            print(f"A) {option1['name']} is a {option1['description']} from {option1['country']}")
            print(art.vs)
            print(f"B) {option2['name']} is a {option2['description']} from {option2['country']}")
            player_choice = input("\nWhich has more followers? Type 'A' or 'B': ")
            result = compare_choices(option1,option2,player_choice)
            if result[0] == 'win':
                print('\nCorrect! Keep going\n')
                option1 = result[1]
                option2 = generate_choice()
                correct_count += 1
            else:
                print('\nWrong. Game Over')
                is_correct = False
        print(f"You scored {correct_count}")
    
game()