# # import random

# # top_of_range = input('Type a Number')
# # guesses = 0

# # if top_of_range.isdigit():
# #     top_of_range = int(top_of_range)

# #     if top_of_range <= 0:
# #         print('Input more than zero')
# #         quit()
# # else:
# #     print('Input a number')
# #     quit()

# # random_number = random.randint(0, top_of_range)

# # while True:
# #     guesses += 1
# #     user_guess = input('Guess')

# #     if user_guess.isdigit():
# #         user_guess = int(user_guess)
# #     else:
# #         print('Input a number')
# #         continue

# #     if user_guess == random_number:
# #         print('Correct')
# #         break
# #     else:
# #         if user_guess > random_number:
# #             print('too much')
# #         else:
# #             print('too little')
    

# import random

# top_of_number = input('type a number')
# guesses = 0

# if top_of_number.isdigit():
#     top_of_number = int(top_of_number)

#     if top_of_number <= 0:
#         print('input more than zero')

# else:
#     print('input a number')
#     quit()

# while True:
#     user_guess = input()
    
#     random_number = random.randint(0, top_of_number)

#     if user_guess == random_number:
#         print('you won')
#         break
#     elif user_guess > random_number:
#         print('too much')
#         guesses += 1
#     else:
#         print('too low')
#         guesses += 1
        
# print('count', guesses)
    

import random

top_of_range = input()  # เป็นโครงสร้าง ต้องอยู่นอก loop
guesses = 0 # เป็นตัวสะสม ต้องอยู่นอก loop

if top_of_range.isdigit():
    top_of_range == int(top_of_range)
else:
    print('type a number')
    quit()

random_number = random.randint(0, top_of_range) # เจนครั้งเดียว อยู่นอกลูป

while True:
    user_guess = input() # เจนใหม่เรื่อยๆ อยู่ในลูป    

    if user_guess == random_number:
       print('correct')
    else:
        if user_guess > random_number:
            print('too much')
            guesses += 1
        else:
            print('too low')
            guesses += 1
            


