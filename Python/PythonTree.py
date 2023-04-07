import os

os.chdir("/Users/hunteradder626")
listofFiles = []

for root, dirs, files in os.walk("."):
    for filename in files:
        listofFiles.append(filename)
        
os.chdir("/Users/hunteradder626/Desktop")

with open ("listoffiles.txt", "w") as f:
    for everyFileName in listofFiles:
        f.write(everyFileName + "\n")


with open ("listoffiles.csv", "w", newline='') as f:
    for everyFileName in listofFiles:
        f.write(everyFileName + "\n")
        