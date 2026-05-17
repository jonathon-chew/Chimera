import os

path = input("Where is the folder? ")
ext = input("What is the file extention you want to move? ")
compileFolder = input("Where do you want to move them all to? ")

for root, dirs, files in os.walk(path):
    for everyFile in files:
        if not everyFile == ".DS_Store":
            eachFile = str(everyFile)
            if "." in eachFile:
                fileExtention = eachFile.split(".")
                if fileExtention[1] == ext:
                    print(everyFile)
                    source = os.path.join(root, everyFile)
                    destination = os.path.join(compileFolder, everyFile)
                    if not os.path.exists(destination):
                        os.rename(source, destination)
                        print(f"{source} was moved to {destination}")