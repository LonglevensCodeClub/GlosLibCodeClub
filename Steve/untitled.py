
import glob
import os

def doDirectory(dir):
	contents = glob.glob(dir)

    for item in contents:
		if (os.path.isDir(item):
			doDirectory(item)
		elseif (os.path.isFile(item)):
		    print("File: " + item)
		    
		
