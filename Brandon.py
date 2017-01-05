import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  

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
     filename, filetype = os.path.spltext(file_list[n])
     
     # Round the corners with radius = 30% of short side
     new_image = round_corners(image_list[n],.30)
     # Save the altered image, using PNG to retain transparency
     new_image_filename = os.path.join(new_directory,filename + '.png')
     new_image.save(new_image_filename)