from __future__ import print_function
def editPicture():
    '''Runs a menu for you to choose which functions you want to run
    takes no parameters. The program will ask you for needed parameters
    when you choose an option.'''
    #initializes menuOption to 0: a value that shouldn't ever be used except for
    #here
    
    menuOption = 0
    while menuOption is not 4:
        
        #Gives the user a chance to input and tells them what each input will do.
        try:
            print('\nEnter 1 for Adding a Border\n\n'
            + 'Enter 2 for Adding Family Watermark\n\n'
            + 'Enter 3 for Adding both a Border and the Watermark\n\nEnter 4 to quit.')
            menuOption = int(raw_input("Choice: "))
            print(menuOption)

            #Now that the user has chosen which input, test if it is in range.
            if menuOption < 1 or menuOption > 4:
                print('You must enter a number between 1 and 4. Try again.')
                
            elif menuOption == 1:
                print('something1')
                #Insert border function here
                
            elif menuOption == 2:
                print('something2')
                #Insert watermark function here
                
            elif menuOption == 3:
                print('something3')
                #Insert code to run both programs
            
        #If the user didn't enter a number, which will cause the program to be annoyed...
        except ValueError:
            print('You must enter a number. Try again.')