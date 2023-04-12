import os

folder = "/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Documents/Scripts/VBA/Subs"

for x in os.listdir(folder):
    if 'txt' in x:
        origionalName = os.path.join(folder, x)
        oldName = x.split('.')
        oldName = oldName[0]
        newName = oldName + ".bas"
        newName = os.path.join(folder, newName)
        print(newName)
        os.rename(origionalName, newName)