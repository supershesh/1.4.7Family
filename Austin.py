#Austin
#This file will make the desired image opaque

import matplotlib.pyplot as plt 
import os.path
import numpy as np 

import PIL
import os.path  

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
         filename = os.path.join(directory, absolute_filename)
         img = plt.imread(filename)
         height = len(img)
         width = len(img[0])
         for row in range (height):
                for column in range (width):
                    x = img[row][column][0]
                    y = img[row][column][1]
                    z = img[row][column][2]
                    img[row][column] = [x,y,z,128]
      
    except IOError: 
        pass
    else:
        print "Wrong file extension used, the image opacity won't be changed!"
    #Give a warning if the wrong file extension is used



'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()