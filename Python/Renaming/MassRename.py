import os
import re

# path = '/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Documents/Scripts/Python'
path = "/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Documents/"
listofFoleders = []

checkfilename = []

os.chdir(path)
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename != ".DS_Store":
            checkfilename = re.split('\?|!|:|\*|>|<|"', filename)
            checkfilename = ''.join(checkfilename)
            # print(checkfilename)
            # print(filename)
            if checkfilename == filename:
                pass
            else:
                newFileName = ''.join(checkfilename)
                destination = os.path.join(root, newFileName)
                orgionalSource = os.path.join(root, filename)
                os.rename(orgionalSource, destination)
                print(f"Changed {filename} to {newFileName}")