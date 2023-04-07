import os

path = "/users/hunteradder626/desktop/python/projects"

ext = "py"

for root, dirs, files in os.walk(path):
    for everyFile in files:
        if not everyFile == ".DS_Store":
            eachFile = str(everyFile)
            if "." in eachFile:
                fileExtention = eachFile.split(".")
                if fileExtention[1] == ext:
                    print(everyFile)