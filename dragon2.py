__author__ = 'ankurs'

import random
import time

def intro():
     print('You are in a land full of dragons. In front of you, \nyou see two caves. In one cave, the dragon is friendly \nand will share his treasure with you. The other dragon \nis greedy and hungry, and will eat you on sight. \n')
     option = input('Which cave will you go into? (1 or 2)')
     return option

def cave(selection):
     print('You approach the cave...')
     time.sleep(2)
     print('It is dark and spooky...')
     time.sleep(2)
     print('A large dragon jumps out in front of you! He opens his jaws and...')
     time.sleep(2)
