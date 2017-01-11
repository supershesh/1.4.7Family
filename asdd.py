def get_images(directory=None):
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