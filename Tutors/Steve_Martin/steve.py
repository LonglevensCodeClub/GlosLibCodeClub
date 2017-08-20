
import glob
import os
from PIL import Image
from PIL.ExifTags import TAGS

def doDirectory(dir):
    contents = glob.glob(dir + "/*")

    for item in contents:
        if (os.path.isdir(item)):
            print("Dir: " + item)
            doDirectory(item)
        elif (os.path.isfile(item)):
            print("File: " + item)
            if (item.endswith(".gif")):
                i = Image.open(item)
                info = i._getexif()
                for tag, value in info.items():
                    print(TAGS.get(tag, tag))
        else:
            print("### Skipping: " + item)


doDirectory("/home/pi")
 
