#Austin
#This file will make the desired image opaque

import matplotlib.pyplot as plt 
import os.path
import numpy as np 

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.gif')
# Read the image data into an array
img = plt.imread(filename)

height = len(img)
width = len(img[0])
#Check for proper extension
if filename.endswith('.gif'):
    try:
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