from random import randint

number = randint(1, 100)
guess = ""

def is_number(x):
    """
    Checks if the string is a number
    :param x: the string to be checked
    :return: True if the string is a number
    """
    return x.isdigit()

print(number)
while True:
    guess = input("Guess a number: ")
    if is_number(guess) == True:
        if int(guess) > number:
            print("Too big!")
        elif int(guess) < number:
            print("Too small!")
        else:
            print("You win!")
            break
    else:
        print("It's not a number!")
