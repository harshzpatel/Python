import random, os

while True:  # infinity loop
    os.system('cls')  # clear the screen

    print('Note:\nYou have to guess the no. in the range 1 to 10')

    scoreboard = '''
-------------------------------------------------------------------------------

    Your score: {}
    Chances left: {}
    Entered no.: {}

-------------------------------------------------------------------------------
'''

    n = random.randrange(1, 11)
    score = 30
    chances = 3
    inp = '__'

    while True:
        print(scoreboard.format(score, chances, inp))

        if chances == 0:
            os.system('cls')
            print(scoreboard.format(score, chances, inp))
            print('You lost!\nThe no. was', n)
            input('Press enter to play again')
            break  # exit the loop

        else:
            pass  # do nothing

        inp = int(input('\nGuess the no.- '))

        if inp == n:
            os.system('cls')  # clear the screen
            print(scoreboard.format(score, chances, inp))
            print('Your guess was right!')
            input('\nPress enter to play again')
            break  # exit the loop

        elif n > inp:
            os.system('cls')  # clear the screen
            score -= 10
            chances -= 1
            print('Wrong guess... try again')
            print('\nTip:\nThe no. is greater than that you entered')

        else:
            os.system('cls')  # clear the screen
            score -= 10
            chances -= 1
            print('Wrong guess... try again')
            print('\nTip:\nThe no. is smaller than that you entered')
