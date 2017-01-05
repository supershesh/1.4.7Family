from __future__ import print_function
from builtins import input
def editPicture():
    '''Runs a menu for you to choose which functions you want to run
    takes no parameters. The program will ask you for needed parameters
    when you choose an option.'''
    #initializes menuOption to 0: a value that shouldn't ever be used except for
    #here.
    menuOption = 0
    print('Enter 1 for Adding a Border\n\nEnter 2 for Adding Family Watermark\n\n'
    + 'Enter 3 for Adding both a Border and the Watermark\n\nEnter 4 to quit.')
    menuOption = raw_input("Choice: ")