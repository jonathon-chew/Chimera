import os

file = "/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Documents/Scripts/VBA/Cheat_Sheets/VBA-Cheat-Sheet.txt"

with open (file, 'r') as f:
    contents = f.read()

splitContents = contents.split('\n')

prevInt = 0
subprocesses = []

for i, x in enumerate(splitContents):
    if "End Sub" in x:
        mars = '\n'.join(splitContents[prevInt:i])
        prevInt = i
        subprocesses.append(mars)

os.chdir("/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Documents/Scripts/VBA/Cheat_Sheets/Subs")

for p, i in enumerate(subprocesses):
    fileName = subprocesses[p].split("\n")
    fileName = fileName[3].split(" ")
    fileName = fileName[1].split("(")
    fileName = fileName[0] + ".txt"
    with open (fileName, 'w') as w:
        w.write(i)
        w.write("End Sub")