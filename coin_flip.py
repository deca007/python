__author__ = 'ak'

import random
import time

print('I will flip a coin 1000 times. Guess how many times it will come up heads. \n(Press enter to begin)')
input()
flip = 0
head = 0
tail = 0
while flip < 1000:
        if random.randint(1,2) == 1:
            head += 1
            flip += 1
        else:
            tail += 1
            flip += 1
        if flip == 100:
            print('Out of 100 flips, There were '+ str(head) + ' heads and ' + str(tail) + ' tails so far ')
            print('Coin flip going on .....')
            time.sleep(2)
        if flip == 900:
            print('Out of 900 flips, There were '+ str(head) + ' heads and ' + str(tail) + ' tails so far ')
            print('Coin flip going on .....')
            time.sleep(2)

print('Out of 1000 flips, There were '+ str(head) + ' heads and ' + str(tail) + ' tails')
print('Were you close?')



