__author__ = 'ankurs'

import random
guess_num = random.randint(1,20)
name = input("Enter your name? ")
if name == "Sanyukta" or name == "sanyukta":
    print("Hello Saand, I have a number between 1 and 20. Can you guess it?")
else:
    print("Hello " +name + ", I have a number between 1 and 20. Can you guess it? ")
guess_taken = 0

while guess_taken < 6:
    num = int(input("Take a guess "))
    guess_taken += 1

    if num > guess_num:
            print("Too high, take another guess")
    if num < guess_num:
            print('Too low, take another guess')
    if num == guess_num:
                break
if num == guess_num:
    print('Good job. You solved this in ' + str(guess_taken) + ' guesses')
else:
    print('You failed. I was thinking of ' + str(guess_num) + 'number')






