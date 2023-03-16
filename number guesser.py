import random

top_of_range = input('Type a Number')
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Input more than zero')
        quit()
else:
    print('Input a number')
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input('Guess')

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Input a number')
        continue

    if user_guess == random_number:
        print('Correct')
        break
    else:
        if user_guess > random_number:
            print('too much')
        else:
            print('too little')
    