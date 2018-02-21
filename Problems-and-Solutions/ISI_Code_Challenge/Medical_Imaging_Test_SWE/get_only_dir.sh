# get_only_dir returns True if there is more than 1 subdirectory for the input path
# will return False if the input path is not valid or if tha path is empty.

#!/usr/bin/bash

echo "Please enter your path:"

read path

# list out all the paths with at least one subdirectory, if produce error stash it to /dev/null
subdirs=$(ls -d $path/*/ 2>/dev/null)

# if there is only one subdirectory listed
if [ "`wc -lw <<< "$subdirs" | xargs`" == "1 1" ]; then
	# echo true and the subdirectory 
        echo "True,\"`echo $subdirs`\""
else
    	echo "False,\"\""
fi