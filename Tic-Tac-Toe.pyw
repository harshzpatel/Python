from tkinter import *

r = Tk()
mainbg = '#0a3d62'
chance = 'X'
game_loop = True

r.title('Tic-Tac-Toe by Harsh')
r.minsize(250, 380)
r.maxsize(250, 380)
r.configure(bg=mainbg, padx=20, pady=0)

btnwidth = 5
btnheight = 2
btnbg = '#2475b0'
btnfg = '#eaf0f1'
btnfont = 'cooperblack 15 bold'


def changevals(btnvalue):  # function to change value of buttons
    global chance

    if game_loop:
        if btnvalue.get() == '':  # if button value is not yet assigned to 'X' or 'Y'
            btnvalue.set(chance)  # set button value

            checkwinner()

            # change chance
            if chance == 'X':
                chance = 'O'
            else:
                chance = 'X'
        else:
            pass
    else:
        statusvalue.set('Press Reset button.')


def checkwinner():
    global game_loop

    # horizontal check
    if b1Value.get() == b2Value.get() == b3Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    elif b4Value.get() == b5Value.get() == b6Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    elif b7Value.get() == b8Value.get() == b9Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    # vertical check
    elif b1Value.get() == b4Value.get() == b7Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    elif b2Value.get() == b5Value.get() == b8Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    elif b3Value.get() == b6Value.get() == b9Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    # diagonal check
    elif b1Value.get() == b5Value.get() == b9Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    elif b3Value.get() == b5Value.get() == b7Value.get() != '':
        statusvalue.set(f'{chance} won!')
        game_loop = False

    elif '' in [b1Value.get(), b2Value.get(), b3Value.get(), b4Value.get(), b5Value.get(), b6Value.get(), b7Value.get(), b8Value.get(), b9Value.get()]:  # if the game is not over
        pass

    else:  # if the game is over without a winner
        statusvalue.set('Draw!')
        game_loop = False


def reset():
    global game_loop

    b1Value.set('')
    b2Value.set('')
    b3Value.set('')
    b4Value.set('')
    b5Value.set('')
    b6Value.set('')
    b7Value.set('')
    b8Value.set('')
    b9Value.set('')
    statusvalue.set('')
    game_loop = True


b1Value = StringVar()
b2Value = StringVar()
b3Value = StringVar()
b4Value = StringVar()
b5Value = StringVar()
b6Value = StringVar()
b7Value = StringVar()
b8Value = StringVar()
b9Value = StringVar()
statusvalue = StringVar()

Label(text='Tic-Tac-Toe', fg='#fbd28b', bg=mainbg, font=('kristen itc', 19, 'bold')).grid(columnspan=3, pady=15)

Button(textvariable=b1Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b1Value)).grid(row=1, padx=1, pady=1, column=0)
Button(textvariable=b2Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b2Value)).grid(row=1, padx=1, pady=1, column=1)
Button(textvariable=b3Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b3Value)).grid(row=1, padx=1, pady=1, column=2)

Button(textvariable=b4Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b4Value)).grid(row=2, padx=1, pady=1, column=0)
Button(textvariable=b5Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b5Value)).grid(row=2, padx=1, pady=1, column=1)
Button(textvariable=b6Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b6Value)).grid(row=2, padx=1, pady=1, column=2)

Button(textvariable=b7Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b7Value)).grid(row=3, padx=1, pady=1, column=0)
Button(textvariable=b8Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b8Value)).grid(row=3, padx=1, pady=1, column=1)
Button(textvariable=b9Value, bg=btnbg, fg=btnfg, activebackground=mainbg, activeforeground=btnbg, border=0, font=btnfont, width=btnwidth, height=btnheight, command=lambda: changevals(b9Value)).grid(row=3, padx=1, pady=1, column=2)

Button(text='Reset', bg='#f3b431', fg='#2f363f', activebackground=mainbg, activeforeground='#f3b431', font=('comic sans ms', 10), width=6, border=0, height=1, command=reset).grid(row=5, column=0)
Button(text='Exit', bg='#ff3031', fg='#2f363f', activebackground=mainbg, activeforeground='#ff3031', font=('comic sans ms', 10), width=6, border=0, height=1, command=r.destroy).grid(row=5, column=2)

Label(textvariable=statusvalue, fg=btnfg, font=('comic sans ms', 12), bg=mainbg).grid(row=4, pady=20, column=0, columnspan=3)

r.mainloop()
