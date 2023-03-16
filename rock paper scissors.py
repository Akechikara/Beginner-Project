import random

user_wins = 0
computer_wins =0

random_number = random.randint(0,2)
options = ['rock','paper','scissors']

while True:
    user_pick = input('Rock / Paper / Scissors or Q to quit')
    user_pick = user_pick.lower()
    if user_pick == 'q':
        break
    computer_pick = options[random_number]

    if user_pick == 'rock' and computer_pick == 'scissors':
        print('You won')
        user_wins += 1
    elif user_pick == 'paper' and computer_pick == 'rock':
        print('You won')
        user_wins += 1
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print('You won')
        user_wins += 1
    else:
        print('You lost')
        computer_wins += 1

print('Your score', user_wins)
print('Computer score', computer_wins)
print('Bye')
    
