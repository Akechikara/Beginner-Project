# print('Welcome to quiz game')

# playing = input('Do you want to play a game?')
# score = 0

# if playing.lower() != 'yes':
#     quit()

# answer = input('What does CPU stand for?')
# if answer.lower() == 'central processing unit':
#     print('Correct')
#     score += 1
# else:
#     print('Incorrect')

# answer = input('What does GPU stand for?')
# if answer.lower() == 'graphic processing unit':
#     print('Correct')
#     score += 1
# else:
#     print('Incorrect')

# answer = input('What does RAM stand for?')
# if answer.lower() == 'random access memory':
#     print('Correct')
#     score += 1
# else: 
#     print('Incorrect')

# answer = input('What does PSU stand for?')
# if answer.lower() == 'power supply':
#     print('Correct')
#     score += 1
# else: 
#     print('Incorrect')

# print('You got ' + str((score/4)*100) + '%')

score = 0

answer = input('อากุมอน')
if answer == 'agumon':
    print('correct')
    score += 1

answer = input('ปิโยมอน')
if answer == 'piyomon':
    print('correct')
    score += 1

answer = input('กาบุมอน')
if answer == 'gabumon':
    print('correct')
    score += 1

print('score = '+ str(score))

