import random

print('---------------------------')
print('    GUESS NUMBER GAME')
print('---------------------------')
print()

correct_number = random.randint(0, 100)

player_name = input('Player what is your name? ')

guess = -1  # Need to set this variable to a value outside the range 0-100,
            # since we use it in the conditional before we ask the user for input.

while guess != correct_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < correct_number:
        print('Sorry {}, your guess of {} was too LOW.'.format(player_name, guess))
    elif guess > correct_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(player_name, guess))
    else:
        print('Excellent work {}, it was {}!'.format(player_name, guess))

print('Done')