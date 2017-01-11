from __future__ import print_function
import PIL
from PIL import ImageDraw
import os.path
import matplotlib.pyplot as plt


def editPicture():
    '''Runs a menu for you to choose which functions you want to run
    takes no parameters. The program will ask you for needed parameters
    when you choose an option.'''
    #initializes menuOption to 0: a value that shouldn't ever be used except for
    #here

    menuOption = 0
    directoryValid = False
    

    directoryChoice = raw_input("Please enter the name of the folder you want to change: ")
    directory = os.path.join(os.getcwd(), directoryChoice)
    
    while menuOption is not 4:
        
        #Gives the user a chance to input and tells them what each input will do.
        try:
            print('\nEnter 1 for Adding a Frame\n\n'
            + 'Enter 2 for Adding Family Watermark\n\n'
            + 'Enter 3 for Adding both a Border and the Watermark\n\nEnter 4 to quit.')
            print(os.getcwd())
            menuOption = int(raw_input("Choice: "))
            print(menuOption)

            #Now that the user has chosen which input, test if it is in range.
            if menuOption < 1 or menuOption > 4:
                print('You must enter a number between 1 and 4. Try again.')
                
            elif menuOption == 1:
                print('something1')
                #Insert border function here
                frame_images(directory)
                
            elif menuOption == 2:
                print('something2')
                #Insert watermark function here
                watermark(False, directory)
            
            elif menuOption == 3:
                print('something3')
                #Insert code to run both programs
                frame_images(directory)
                watermark(True, directory)
                
        #If the user didn't enter a number, which will cause the program to be annoyed...
        except ValueError:
            print('You must enter a number. Try again.')
            

def frame_images(directory=None):
 ''' Saves a modified version of each image in directory.

 Uses current directory if no directory is specified. 
 Puts images in subdirectory 'modified', creating it if needed.
 New image files are of type PNG and have transparent rounded corners.
 '''

 if directory == None:
     directory = os.getcwd() # Use working directory if unspecified

 # Create a new directory 'modified'
 new_directory = os.path.join(os.getcwd(), 'modified')
 try:
     os.mkdir(new_directory)
 except OSError:
     pass # if the directory already exists, proceed 

 # Load all the images
 image_list, file_list = get_images(directory) 

 # Go through the images and save modified versions
 for n in range(len(image_list)):
     # Parse the filename
     filename, filetype = os.path.splitext(file_list[n])
     
     # Round the corners with radius = 30% of short side
     new_image = round_corners(image_list[n],.30)
     # Save the altered image, using PNG to retain transparency
     new_image_filename = os.path.join(new_directory,filename + '.png')
     new_image.save(new_image_filename)
     
     
def round_corners(original_image, percent_of_side):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw one rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius-75,25),(width-radius+75,25),
                            (width-radius+75,height-25),(radius-75,height-25)],
                            fill=(127,0,127,255))

                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
    
def get_images(directory=None):
 ''' Returns PIL.Image objects for all the images in directory.

 If directory is not specified, uses current directory.
 Returns a 2-tuple containing 
 a list with a PIL.Image object for each image file in root_directory,     
 and a list with a string filename for each image file in root_directory
 '''

 if directory == None:
     directory = os.getcwd() # Use working directory if unspecified

 image_list=[] # Initialize aggregators
 file_list = []

 directory_list = os.listdir(directory) # Get list of files
 for entry in directory_list:
     absolute_filename = os.path.join(directory, entry)
     try:
         image = PIL.Image.open(absolute_filename)
         file_list += [entry]
         image_list += [image]
     except IOError:
         pass # do nothing with errors tying to open non-images
 return image_list, file_list
 
 
def watermark(allFunctions = False, directory = None):
    '''Inserts a watermark into the image.
    Takes an boolean argument of if you are going through all the functions'''
    if allFunctions == True:
        directory = os.path.join(os.getcwd(), 'modified')
        
    try:
     os.mkdir(os.path.join(os.getcwd(), 'modified'))
    except OSError:
     pass # if the directory already exists, proceed 
     
    print(directory)
    watermark = PIL.Image.open(os.path.join(os.getcwd(), 'NuamesLogo.png'))
    image_list, file_list = get_images(directory) 
    for n in range(len(image_list)):
     # Parse the filename
        modifiedImage = image_list[n]
        try:
            modifiedImage.paste(watermark, (0, 0), mask=watermark)
            modifiedImage_filename = os.path.join(directory,file_list[n])
            modifiedImage.save(modifiedImage_filename)
        except KeyError:
            pass