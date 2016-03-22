__author__ = 'ak'

import random
import time

def intro():
    print('I will flip a coin 1000 times. Guess how many times it will come up heads. \n(Press enter to begin)')
    input()

def coin_toss():
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
    return head,tail
    #return tail

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    intro()
    total = coin_toss()
    #print(type(total))
    #print(total[0])
    print('Out of 1000 flips, There were '+ str(total[0]) + ' heads and ' + str(total[1]) + ' tails')
    print('Do you want to play again')
    play_again = input()
