# get_only_dir returns True if there is more than 1 subdirectory for the input path
# will return False if the input path is not valid or if tha path is empty.

#!/usr/bin/env python

import sys 
import os
import string

def get_only_dir(directory):
	if directory is None:
		print "False, \"\" " 
		return 

	if os.path.isdir(directory):
		subdir = next(os.walk(directory))[1]
		if len(subdir) == 1:
			subdir = subdir[0]
		 	print "True, ", os.path.join(directory, subdir)
		else:
			print "False, \"\" "
		return 
	
	else:
		print "False, \"\" "
		return  

	
if __name__ == "__main__":
	myDirectory = raw_input('Please enter your path: ')
	get_only_dir(myDirectory)


