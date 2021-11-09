from PIL import Image
from PIL import ImageEnhance
import os

#This code enhaces all the images in a certain directory. Make sure that the directory only has images.

#Input you path file here.
os.getcwd()
os.chdir(r'Insert Directory Here')
os.getcwd()
files_list = os.listdir('.')

#iterates every image file
for index, item in enumerate(files_list):
    if os.path.isfile(item):
        # Opens the image file
        image = Image.open(item)
        #image.show()

        # Enhance Sharpness
        curr_sharp = ImageEnhance.Sharpness(image)
  
        # Sharpness enhanced by a factor of 8.3
        img_sharped = curr_sharp.enhance(2.4)
        curr_sharp = ImageEnhance.Contrast(img_sharped)
        img_sharped = curr_sharp.enhance(1.2)

        # shows updated image in image viewer un-comment it if you want to see the before and after
        #img_sharped.show()
    
        #replaces the current image with the enhanced one.
        img_sharped.save(item)
