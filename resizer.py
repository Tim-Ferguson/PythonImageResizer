
from PIL import Image
import os, sys

path = "/Somel/path/here/"
dirs = os.listdir( path )
#debug print(dirs)
maxWidth = 800 #desired pixel width

def resizeImages():
    for item in dirs:
        #debug print(os.path.isfile(path+item))
        if os.path.isfile(path+item): 
            # debug print(path+item)
            image = Image.open(path+item)
            #debug print(image.size[0])
            wpercent = (maxWidth/float(image.size[0]))
            height = int(float(image.size[1])*float(wpercent))
            f, e = os.path.splitext(path+item)
            imResize = image.resize((maxWidth,height), Image.ANTIALIAS)
            imResize.save(f+'to800wide.png', 'PNG', quality=90)

resizeImages()
print("Finished")