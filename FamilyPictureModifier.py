from __future__ import print_function
import PIL
import os.path
import numpy as np 
import matplotlib.pyplot as plt 

def editPicture():
    '''Runs a menu for you to choose which functions you want to run
    takes no parameters. The program will ask you for needed parameters
    when you choose an option.'''
    #initializes menuOption to 0: a value that shouldn't ever be used except for
    #here
    
    menuOption = 0
    while menuOption is not 5:
        
        #Gives the user a chance to input and tells them what each input will do.
        try:
            print('\nEnter 1 for Adding a Frame\n\n'
            + 'Enter 2 for Adding Family Watermark\n\n'
            + 'Enter 3 for Adding Border\n\n'
            + 'Enter 4 for Adding both a Border and the Watermark\n\nEnter 5 to quit.')
            menuOption = int(raw_input("Choice: "))
            print(menuOption)

            #Now that the user has chosen which input, test if it is in range.
            if menuOption < 1 or menuOption > 5:
                print('You must enter a number between 1 and 5. Try again.')
                
            elif menuOption == 1:
                print('something1')
                #Insert border function here
                frame_images()
                
            elif menuOption == 2:
                print('something2')
                #Insert watermark function here
                
            elif menuOption == 3:
                print('something3')
                #Insert Border function here
            
            elif menuOption == 4:
                print('something4')
                #Insert code to run both programs
            
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
 new_directory = os.path.join(directory, 'modified')
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
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result