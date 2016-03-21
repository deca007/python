__author__ = 'ankurs'

import random
import time

def intro():
    print('You are in a land full of dragons. In front of you, \nyou see two caves. In one cave, the dragon is friendly \nand will share his treasure with you. The other dragon \nis greedy and hungry, and will eat you on sight. \n')

def cave():
    my_cave =''
    while my_cave != '1' and my_cave != '2':
        print('Which cave will you go into? (1 or 2)\n')
        my_cave = input()
    return my_cave

def checkCave(my_choice):
        print('You approach the cave...')
        time.sleep(2)
        print('It is dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps out in front of you! He opens his jaws and...')
        time.sleep(2)
        friend_cave = random.randint(1,2)
        if my_choice == str(friend_cave):
            print('Gives you his treasure')
        else:
            print('Gobbles you down in one bite!')

playAgain ='yes'
while playAgain == 'yes' or playAgain =='y':
    intro()
    caveNum = cave()
    checkCave(caveNum)
    print('Do you want to play again (yes or no)')
    playAgain = input()



