# 1.2 - Guess the number
#

import random

number = random.randint(1, 10)
user = None

while number != user:
    while True:
        try:
            user = int(input("Please guess the number between 1 and 10: "))
        except ValueError:
            print("Sorry, please enter a valid number.")
            continue
        else:
            break
    if user > number:
        print("Your input was a little too high.")
    elif user < number:
        print("Your input was a little too small.")
    else:
        print("Correct!")
