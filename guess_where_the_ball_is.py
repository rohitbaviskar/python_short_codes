"""
There are 3 cups. One cup has a red ball denoted by - 'O'.
The cups are shuffled randomly.
You have to guess where the red ball is.

"""


from random import shuffle

the_list = ['', 'O', '']


def mixer(the_list):
    """
    shuffles the list. rearranges the elememts of list randomly.
    """
    shuffle(the_list)
    return the_list


def player_guess():
    """
    asks for the player input between 0,1,2. If outside of this, it will keep looping untill it gets one out of these 3.
    """
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Please Enter your guess from - 0, 1, 2: ')
    return int(guess)


def check_guess(the_list, guess):
    """
    checks the guess and where the ball is.
    """
    if the_list[guess] == 'O':
        print('Congratulation! Your Guess is Correct.')
    else:
        print('Wrong Guess! Better luck next time.')
        print(the_list)


"""Shuffles the list"""
mixedlist = mixer(the_list)

"""Takes player input"""
guess_in = player_guess()

"""Checks the guess"""
check_guess(the_list, guess_in)
