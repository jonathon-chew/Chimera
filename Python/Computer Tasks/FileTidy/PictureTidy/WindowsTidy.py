import os
import os.path
import time
import datetime

userChoice = input("Where is the folder with the pictures? eg. Users/User/Pictures: ")

path = str(userChoice)
fileNames = []
screenshots = []

def get_the_date(seperatedFileName):
    for date in screenshots:
        fileDate = seperatedFileName[1].split("-")
        print(fileDate)
        return fileDate
        
for i in os.listdir(path):
    fileNames.append(i)

for names in fileNames:
    if os.path.isfile(path + "/" + names):
            # print(names)
            seperatedFileName = names.split()
            fileCreationTime = os.path.getctime(path + "/" + names)
            # print(fileCreationTime)
            fileCreation = time.ctime(fileCreationTime)
            # print(fileCreation)
            fileCreationDateAndTime = datetime.datetime.strptime(fileCreation, "%a %b %d " "%H:%M:%S %Y" )
            fileCreation = str(fileCreationDateAndTime).strip(" ")
            fileCreation = fileCreation[0:10]
            # print(fileCreation)
            yearDate = fileCreation[0:4]
            # print(yearDate)
            monthDate = fileCreation[5:7]
            # print(monthDate)
            dayDate = fileCreation[8:10]
            # print(dayDate)
            
            monthDict = {1:'1. Jan', 2:'2. Feb', 3:'3. Mar', 4:'4. Apr', 5:'5. May', 6:'6. Jun', 
                7:'7. Jul', 8:'8. Aug', 9:'9. Sep', 10:'10. Oct', 11:'11. Nov', 12:'12. Dec'}
            monthDate = monthDict[int(monthDate)]
            
            yearFolder = path + "/" + yearDate
            monthFolder = yearFolder + "/" + monthDate
            dayFolder = monthFolder  + "/" + dayDate
            
            try:
                if not os.path.exists(yearFolder):
                    os.mkdir(yearFolder)
                if not os.path.exists(monthFolder):
                    os.mkdir(monthFolder)
                if not os.path.exists(dayFolder):
                    os.mkdir(dayFolder)
            except OSError:
                pass
                # print ("Creation of the directory %s failed" % dayFolder)
            else:
                pass
                # print ("Successfully created the directory %s " % dayFolder)
                # print("Files ready to be moved")
            # source = path + "/" + names
            # destination = dayFolder + "/" + names 
            # os.rename(source, destination)
        