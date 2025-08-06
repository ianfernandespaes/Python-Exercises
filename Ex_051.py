from random import randint
guesses = 0
computer = randint(0, 10)
print('I am your computer... I just thought of a number between 0 and 10.')
print('Can you guess what it was?')
correct = False
while not correct:
    player = int(input('What is your guess? '))
    guesses += 1
    if player == computer:
        correct = True
    else:
        if player < computer:
            print('Higher... Try again.')
        else:
            print('Lower... Try again.')

print('You got it right with {} guesses'.format(guesses))
