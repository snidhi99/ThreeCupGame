from random import shuffle

# CHOOSE LIST OF BALLS
mylist = [' ', ' ', '0']


# SHUFFLE LIST
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# TAKE A GUESS


def take_guess():
    guess = ' '

    while guess not in ['0', '1', '2']:
        guess = input("What's your choice (0,1,2)? ")
    return int(guess)

# CHECK GUESS


def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print("Right guess!")
        print(mylist)
    else:
        print("Wrong guess, try again!")
        print(mylist)


shuffle_list(mylist)
guess = take_guess()
check_guess(mylist, guess)
