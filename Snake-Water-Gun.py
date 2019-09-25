import random, os

choices = ('Snake', 'Water', 'Gun')
yourScore = 0
compScore = 0
chances = 10

scoreboard = '''
-------------------------------------------------------------------------------

    Your score: {}
    Computer's score: {}
    Chances left: {}

-------------------------------------------------------------------------------
'''

print('Rule: Snake > Water > Gun > Snake')
input('Are you ready!, Press enter to play the game')  # wait for the user response

while chances > 0:
    os.system('cls')  # clear screen
    print(scoreboard.format(yourScore, compScore, chances))

    compChoice = random.choice(choices)
    yourChoice = input('What you want - Snake(s), Water(w), Gun(g)- ')

    if yourChoice.lower() == 's':
        yourChoice = 'Snake'
    elif yourChoice.lower() == 'w':
        yourChoice = 'Water'
    elif yourChoice.lower() == 'g':
        yourChoice = 'Gun'
    else:  # if value entered is not valid
        print('\nUnknown value entered...')
        input('Press enter to exit the game')  # wait for the user response
        exit()

    print(f"\nYour choice- {yourChoice}")
    print(f"Computer's choice- {compChoice}")

    if choices.index(compChoice) - choices.index(yourChoice) == 2 or choices.index(yourChoice) - choices.index(compChoice) == 2:  # if the choices are Snake and Gun
        if yourChoice == 'Gun':
            yourScore += 10
            compScore -= 5
            print('\nYou win!')

        else:
            yourScore -= 5
            compScore += 10
            print('\nYou lose...')
            if chances > 1:
                print(f"Don't worry, you have {chances - 1} chances more!")

    elif choices.index(yourChoice) > choices.index(compChoice):  # high index means low power
        yourScore -= 5
        compScore += 10
        print('\nYou lose...')
        if chances > 1:
            print(f"Don't worry, you have {chances - 1} chances more!")

    elif choices.index(yourChoice) < choices.index(compChoice):  # low index means high power
        yourScore += 10
        compScore -= 5
        print('\nYou win!')

    elif yourChoice == compChoice:  # if both the choices are same
        print('\nDraw!')

    chances -= 1  # reduce the chances each time

    input('\nPress enter to continue')  # wait for the user response

os.system('cls')  # clear screen
print(scoreboard.format(yourScore, compScore, chances))

print('-------------------------------- Final result ---------------------------------')
if yourScore > compScore:
    print('\nAt last, You Won!')

elif yourScore < compScore:
    print('\nYou lose...')
    print('Have a good luck next time...')
else:
    print('Draw!')

input('\nPress enter to exit the game')  # wait for the user response
