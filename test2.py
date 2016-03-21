__author__ = 'ankurs'

import os
from subprocess import call

print(os.getcwd())
print(os.getuid())
print(os.getenv('PATH'))

os.system('ls -al')
in1 = input('Hit Enter : ')
call(['ls', '-al'])
