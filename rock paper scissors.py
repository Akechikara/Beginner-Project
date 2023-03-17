# import random

# user_wins = 0
# computer_wins =0

# options = ['rock','paper','scissors']

# while True:
#     user_pick = input('Rock / Paper / Scissors or Q to quit')
#     user_pick = user_pick.lower()
#     if user_pick == 'q':
#         break
    
#     if user_pick not in options:
#         continue
    
#     random_number = random.randint(0,2)
#     computer_pick = options[random_number]

#     if user_pick == 'rock' and computer_pick == 'scissors':
#         print('You won')
#         user_wins += 1
#     elif user_pick == 'paper' and computer_pick == 'rock':
#         print('You won')
#         user_wins += 1
#     elif user_pick == 'scissors' and computer_pick == 'paper':
#         print('You won')
#         user_wins += 1
#     else:
#         print('You lost')
#         computer_wins += 1

# print('Your score', user_wins)
# print('Computer score', computer_wins)
# print('Bye')
    

import random

user_wins = 0
com_wins = 0


options = ['rock','paper','scissors']

while True:
    user_pick = input()
    random_number = random.randint(0,2)
    com_pick = options[random_number]

    if user_pick == 'rock' and com_pick == 'scissors':
        print('you won')
        user_wins += 1
    elif user_pick == 'paper' and com_pick == 'rock':
        print('you won')
        user_wins += 1
    elif user_pick == 'scissors' and com_pick == 'paper':
        print('you won')
        user_wins += 1
    else:
        print('you lost')
        com_wins += 1