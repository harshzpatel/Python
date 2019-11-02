from tkinter import *
from random import randint

r = Tk()

mainbg = '#001b2e'
canvasbg = '#0a3d62'
snakecolour = '#78e08f'
foodcolor = '#e55039'
status = StringVar()
direction = 'right'
gamestarted = False
activecells = [(80, 90, 90, 100), (90, 90, 100, 100), (100, 90, 110, 100)]  # list of active cells
score = 0
timedelay = 205  # time(in milliseconds) taken by snake to move one cell

r.configure(bg=mainbg, padx=15, pady=15)
r.minsize(250, 350)
r.title('Snake by Harsh')


def move():  # function to move the snake in a particular direction
    global gamestarted, score, timedelay
    gamestarted = True
    status.set(f'Score: {score}')
    x1, y1, x2, y2 = activecells[-1]  # head of snake

    if direction == 'right':
        if x2 < 200:
            head = (x1 + 10, y1, x2 + 10, y2)
        else:
            head = (0, y1, 10, y2)

    elif direction == 'left':
        if x1 > 0:
            head = (x1 - 10, y1, x2 - 10, y2)
        else:
            head = (190, y1, 200, y2)

    elif direction == 'up':
        if y1 > 0:
            head = (x1, y1 - 10, x2, y2 - 10)
        else:
            head = (x1, 190, x2, 200)

    else:  # if direction = 'down'
        if y2 < 200:
            head = (x1, y1 + 10, x2, y2 + 10)
        else:
            head = (x1, 0, x2, 10)

    c.create_rectangle(head, fill=snakecolour, outline=canvasbg)  # make a new cell i.e. the head

    if head == food:  # if the snake eats the food
        score += 100  # increase the score
        if timedelay > 5:
            timedelay -= 5  # decrease the time taken by snake to move one cell i.e. increase its speed
        makefood()
    else:
        c.create_rectangle(activecells[0], fill=canvasbg, outline=canvasbg)  # remove tale i.e. the last cell
        activecells.pop(0)  # also remove the cell coordinates from activecells list

    if head in activecells:  # if snake bites itself
        c.create_text(100, 100, text='Game Over!', fill='#eb2f06', font=('comic sans ms', 20))
        status.set(f'Score: {score}\nResetting game in 3 secs')
        r.after(3000, reset)
    else:
        activecells.append(head)  # add the coordinates of the head to the activecells list
        r.after(timedelay, move)


def changeDirection(d):  # function to change the direction of the snake
    global direction

    if gamestarted:  # change the direction only if the game is started
        if (d == 'right' and direction == 'left') or (d == 'left' and direction == 'right'):  # if the new direction is opposite to previous
            pass  # do nothing
        elif (d == 'up' and direction == 'down') or (d == 'down' and direction == 'up'):  # if the new direction is opposite to previous
            pass  # do nothing
        else:
            direction = d  # change the direction


def makefood():
    global food
    x1, y1 = (randint(0, 19) * 10, randint(0, 19) * 10)  # assign random coordinates for food
    food = (x1, y1, x1 + 10, y1 + 10)  # coordinates of food
    if food in activecells:  # if the random coordinates lie on the snake
        makefood()  # make food again
    else:
        c.create_rectangle(food, fill=foodcolor, outline=canvasbg)  # make food


def reset():  # function to reset the game
    global gamestarted, activecells, score, timedelay, direction
    gamestarted = False
    score = 0
    timedelay = 205
    direction = 'right'
    activecells = [(80, 90, 90, 100), (90, 90, 100, 100), (100, 90, 110, 100)]
    c.create_rectangle(0, 0, 200, 200, fill=canvasbg)  # clear the canvas
    c.create_rectangle(80, 90, 90, 100, fill=snakecolour, outline=canvasbg)
    c.create_rectangle(90, 90, 100, 100, fill=snakecolour, outline=canvasbg)
    c.create_rectangle(100, 90, 110, 100, fill=snakecolour, outline=canvasbg)
    makefood()
    status.set('Press enter to play the game!')


def doNothing():
    pass


# bind keyboard keys and assign them functions
r.bind('<Right>', lambda x: changeDirection('right'))
r.bind('<Left>', lambda x: changeDirection('left'))
r.bind('<Up>', lambda x: changeDirection('up'))
r.bind('<Down>', lambda x: changeDirection('down'))
r.bind('<Return>', lambda x: move() if not gamestarted else doNothing())

Label(text='Snake', font=('harrington', 30), bg=mainbg, fg='#fad390').pack()  # heading
c = Canvas(width=200, height=200, bg=canvasbg, highlightbackground='#fad390')
c.pack(pady=10)

#  make initial cells of the snake
c.create_rectangle(80, 90, 90, 100, fill=snakecolour, outline=canvasbg)
c.create_rectangle(90, 90, 100, 100, fill=snakecolour, outline=canvasbg)
c.create_rectangle(100, 90, 110, 100, fill=snakecolour, outline=canvasbg)
makefood()

status.set('Press Enter to start the game!')
Label(textvariable=status, bg=mainbg, fg='#f6b93b', font=('comic sans ms', 10)).pack()

r.mainloop()
