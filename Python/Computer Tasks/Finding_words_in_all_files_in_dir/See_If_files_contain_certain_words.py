import os
from pathlib import Path

path = "/Users/hunteradder626/Desktop/"

filesWithDesktopIn = []

for root, dirs, files in os.walk(path):
    for everyFile in files:
        if everyFile !=  ".DS_Store":
            filePath = os.path.join(root, everyFile)
            if os.path.isfile(filePath):
                # if Path(filePath).suffix == ".py":
                    # print(f"Checking {filePath}")
                    try:
                        with open(filePath, "r") as f:
                            desktopCheck = f.read()
                            if "Desktop" in desktopCheck or "desktop" in desktopCheck:
                                # print(f"Found: {filePath}")
                                filesWithDesktopIn.append(filePath)
                    except:
                        print(f"Couldn't for file {filePath}")

os.chdir("/Users/hunteradder626/Desktop/Python/Projects/Works/Computer_Management/Finding_words_in_all_files_in_dir")
with open ('Python_Files_With_Desktop_In.txt', 'w') as f:
    for everyFileListed in filesWithDesktopIn:
        f.write(everyFileListed)
        f.write("\n")