import os
import re

path = input("What is the file path?\nThis will impact all files in the dir and subdirs?\n")

if not os.path.isdir(path):
    print(f"The path {path} is not a dir")
    exit(1)

listofFoleders, checkfilename = [], []

os.chdir(path)
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename == ".DS_Store":
            continue
        
        checkfilename = re.split('\?|!|:|\*|>|<|"', filename)
        checkfilename = ''.join(checkfilename)

        if checkfilename == filename:
            pass
        else:
            newFileName = ''.join(checkfilename)
            destination = os.path.join(root, newFileName)
            orgionalSource = os.path.join(root, filename)
            os.rename(orgionalSource, destination)
            print(f"Changed {filename} to {newFileName}")