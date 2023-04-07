from genericpath import isfile
import os
import shutil

# location = input("Where is the project you need to prepare? ")
location = "/Users/hunteradder626/Desktop/Python/Projects/Learning/Computer_Management/PrepareAFileForGitHub"
listOfFiles = []
dependancies = []

for file in os.listdir(location):
    if os.path.isfile(os.path.join(location, file)):
        listOfFiles.append(file)

for files in listOfFiles:
    print(listOfFiles)
    if files != ".DS_Store":
        os.chdir(location) 
        with open (files, "r") as f:
            contents = f.readlines()

for everyLine in contents:
    if "import " in everyLine:
        dependancies.append(everyLine)
try:
    os.mkdir("Git_Hub")
except:
    print("Github already exists")

for everyDependancy in dependancies:
    everyDependancy = everyDependancy.strip()
    os.chdir(os.path.join(location, "Git_Hub"))
    with open ("requirements.txt", 'a') as c:
        c.write(everyDependancy + "\n")
    shutil.copy((location+"/"+files), os.path.join(location, "Git_Hub"))

print(dependancies)    

# with open (files, "at") as h:
#     h.readline()