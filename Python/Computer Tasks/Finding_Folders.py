import os

counter = 0
listOfFolders = []
listofEveryFolder = []

os.chdir("/Users/hunteradder626")

#get all folders and files
for eachFolder in os.listdir():
    if eachFolder != ".DS_Store":
        counter = counter + 1
        # print(f"Folder {counter} {eachFolder} ")
        listOfFolders.append(eachFolder)
        listofEveryFolder = listOfFolders

x = 1
newlistOfFolders = []

# while x > 100:
for eachItem in listOfFolders:
    if eachItem != ".DS_Store":
        print (x)
        x = x + 1
        newlistOfFolders.append(eachItem)
    for listItem in newlistOfFolders:
        pass
    # x = x + 1

# for listOfFolders[0] in listOfFolders[len(listOfFolders)]:
#     print(listOfFolders)           

print(listOfFolders)