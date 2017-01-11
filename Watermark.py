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