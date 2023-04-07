import os

location = input (f"Where is the folder that you would like to tidy? ")
os.chdir(location)

fileExtentions = []

for everyFile in os.listdir(location):
    if os.path.isfile(location + "/" + everyFile):
        if everyFile != ".DS_Store":
            if everyFile != "localized":
                everyFile = everyFile.rpartition(".")
                fileExtentions.append(everyFile[2].title())
                fileExtentions = list(dict.fromkeys(fileExtentions))

for everyExtention in fileExtentions:
    try:
        os.mkdir(everyExtention)
    except:
        print("Folder already exists")

for moveFile in os.listdir(location):
    if os.path.isfile(location + "/" + moveFile):
        if moveFile != ".DS_Store":
            if moveFile != "localized":
                source = os.path.join(location, moveFile)
                print(f"The source is: {source}")
                moveFile = moveFile.rpartition(".")
                destination = location + "/" + moveFile[2].title() + "/" + moveFile[0] + "." + moveFile[2]
                print(f"The destination is: {destination}")
                print("#############################")
                try:
                    os.rename(source, destination)
                except:
                    print(f"I couldn't do anything with {moveFile}")