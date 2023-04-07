import os
import shutil

# shutil.rmtree("/Users/hunteradder626/desktop/Backup")

origionalLocation = "/Users/hunteradder626/Desktop/Python/Projects"
newLocation = "/Users/hunteradder626/Desktop/BackUp/Projects"

# getting all the files in the source directory
files = os.listdir(origionalLocation)

shutil.copytree(origionalLocation, newLocation)

origionalLocation = "/Users/hunteradder626/Desktop/Python/Documentation"
newLocation = "/Users/hunteradder626/Desktop/BackUp/Documentation"

# getting all the files in the source directory
files = os.listdir(origionalLocation)

shutil.copytree(origionalLocation, newLocation)